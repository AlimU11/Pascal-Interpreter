from NodeVisitor import NodeVisitor
from Parser import Parser
from ScopedSymbolTable import ScopedSymbolTable
from Symbol import ProcedureSymbol, VarSymbol


class SemanticAnalyzer(NodeVisitor):
    def __init__(self, text):
        self.parser = Parser(text)
        self.current_scope: ScopedSymbolTable = None
        self.scopes = []

    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_Program(self, node):
        global_scope = ScopedSymbolTable(
            scope_name='global',
            scope_level=1,
            enclosing_scope=None,
        )

        global_scope._init_builtins()

        self.current_scope = global_scope
        self.scopes.append(global_scope)

        self.visit(node.block)

        self.current_scope = self.current_scope.enclosing_scope

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_Num(self, node):
        pass

    def visit_UnaryOp(self, node):
        self.visit(node.expr)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_NoOp(self, node):
        pass

    def visit_VarDecl(self, node):
        type_name = node.type_node.value
        type_symbol = self.current_scope.lookup(type_name)

        var_name = node.var_node.value
        var_symbol = VarSymbol(var_name, type_symbol)

        if self.current_scope.lookup(var_name, current_scope_only=True) is not None:
            raise Exception(
                "Error: Duplicate identifier '%s' found" % var_name,
            )

        self.current_scope.insert(var_symbol)

    def visit_Assign(self, node):
        var_name = node.left.value
        var_symbol = self.current_scope.lookup(var_name)

        if var_symbol is None:
            raise NameError(repr(var_name))

        self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        var_symbol = self.current_scope.lookup(var_name)

        if var_symbol is None:
            raise NameError(repr(var_name))

    def visit_ProcedureDecl(self, node):
        proc_name = node.proc_name
        proc_symbol = ProcedureSymbol(proc_name)

        self.current_scope.insert(proc_symbol)

        procedure_scope = ScopedSymbolTable(
            scope_name=proc_name,
            scope_level=self.current_scope.scope_level + 1,
            enclosing_scope=self.current_scope,
        )

        self.scopes.append(procedure_scope)
        self.current_scope = procedure_scope

        for param in node.params:
            param_type = self.current_scope.lookup(param.type_node.value)
            param_name = param.var_node.value
            var_symbol = VarSymbol(param_name, param_type)
            self.current_scope.insert(var_symbol)
            proc_symbol.params.append(var_symbol)

        self.visit(node.block_node)
        self.current_scope = self.current_scope.enclosing_scope

    def analyze(self):
        tree = self.parser.parse()
        self.visit(tree)

        for scope in self.scopes:
            print(
                f'Scope name: {scope.scope_name:8}, '
                f'Scope level: {scope.scope_level:1}, '
                f'Parent scope: {scope.enclosing_scope.scope_name if scope.enclosing_scope else None}',
            )

        return tree
