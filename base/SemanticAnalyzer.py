from base.Error import ErrorCode, SemanticError
from base.NodeVisitor import NodeVisitor
from base.Parser import Parser
from base.ScopedSymbolTable import ScopedSymbolTable
from base.Symbol import BuiltInProcedureSymbol, ProcedureSymbol, Symbol, VarSymbol


class SemanticAnalyzer(NodeVisitor):
    def __init__(self, text):
        self.parser = Parser(text)
        self.current_scope: ScopedSymbolTable
        self.scopes = []

    def error(self, error_code, token):
        raise SemanticError(error_code, token, message=f'{error_code.value} -> {token}')

    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_Program(self, node):
        builtins_scope = ScopedSymbolTable(
            scope_name='builtins',
            scope_level=0,
            enclosing_scope=None,
        )

        builtins_scope._init_builtins()
        program_name = node.name
        builtins_scope.insert(Symbol(program_name))
        self.scopes.append(builtins_scope)

        global_scope = ScopedSymbolTable(
            scope_name='global',
            scope_level=1,
            enclosing_scope=builtins_scope,
        )

        self.current_scope = global_scope
        self.scopes.append(global_scope)

        self.visit(node.block)

        self.current_scope = self.current_scope.enclosing_scope.enclosing_scope

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

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

        if self.current_scope.lookup(var_name, current_scope_only=True):
            self.error(
                error_code=ErrorCode.DUPLICATE_ID,
                token=node.var_node.token,
            )

        self.current_scope.insert(var_symbol)

    def visit_Assign(self, node):
        self.visit(node.right)
        self.visit(node.left)

    def visit_Var(self, node):
        var_name = node.value
        var_symbol = self.current_scope.lookup(var_name)

        if var_symbol is None:
            self.error(
                error_code=ErrorCode.ID_NOT_FOUND,
                token=node.token,
            )

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
            proc_symbol.formal_params.append(var_symbol)

        self.visit(node.block_node)
        self.current_scope = self.current_scope.enclosing_scope
        proc_symbol.block_ast = node.block_node

    def visit_Num(self, node):
        pass

    def visit_UnaryOp(self, node):
        pass

    def visit_ProcedureCall(self, node):
        proc_symbol = self.current_scope.lookup(node.proc_name)

        if proc_symbol is None:
            self.error(
                error_code=ErrorCode.ID_NOT_FOUND,
                token=node.token,
            )

        if not isinstance(proc_symbol, BuiltInProcedureSymbol):
            if len(node.actual_params) != len(proc_symbol.formal_params):
                self.error(
                    error_code=ErrorCode.WRONG_ARGUMENTS_NUMBER,
                    token=node.token,
                )

        for param_node in node.actual_params:
            self.visit(param_node)

        node.proc_symbol = proc_symbol

    def analyze(self):
        tree = self.parser.parse()
        self.visit(tree)
        return tree
