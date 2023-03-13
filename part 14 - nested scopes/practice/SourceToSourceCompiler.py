from NodeVisitor import NodeVisitor
from ScopedSymbolTable import ScopedSymbolTable
from Symbol import ProcedureSymbol, Symbol, VarSymbol


class SourceToSourceCompiler(NodeVisitor):
    def __init__(self):
        self.current_scope = None
        self.compiled = None

    def visit_Block(self, node):
        return '\n'.join(
            [self.visit(declaration) for declaration in node.declarations]
            + [
                '\nBEGIN',
                '   ' + self.visit(node.compound_statement),
                'END',
            ],
        )

    def visit_Program(self, node):
        builtins_scope = ScopedSymbolTable(
            scope_name='builtins',
            scope_level=0,
            enclosing_scope=None,
        )

        builtins_scope._init_builtins()
        program_name = node.name
        builtins_scope.insert(Symbol(program_name))

        global_scope = ScopedSymbolTable(
            scope_name='global',
            scope_level=1,
            enclosing_scope=builtins_scope,
        )

        self.current_scope = global_scope

        self.compiled = ''.join(
            [
                f'PROGRAM <{program_name}0>;\n',
                self.visit(node.block),
                f'; {{END OF {program_name}}}',
            ],
        )

        self.current_scope = self.current_scope.enclosing_scope.enclosing_scope

    def visit_Compound(self, node):
        return '\n'.join(
            [self.visit(child) for child in node.children if self.visit(child) is not None],
        )

    def visit_NoOp(self, node):
        pass

    def visit_BinOp(self, node):
        return f'{self.visit(node.left)} {node.op.value} {self.visit(node.right)}'

    def visit_ProcedureDecl(self, node):
        proc_name = node.proc_name
        proc_symbol = ProcedureSymbol(proc_name)
        self.current_scope.insert(proc_symbol)

        procedure_scope = ScopedSymbolTable(
            scope_name=proc_name,
            scope_level=self.current_scope.scope_level + 1,
            enclosing_scope=self.current_scope,
        )

        self.current_scope = procedure_scope

        result_str = f'PROCEDURE <{proc_name}{self.current_scope.scope_level}>'

        formal_params = []

        for param in node.params:
            param_type = self.current_scope.lookup(param.type_node.value)
            param_name = param.var_node.value
            var_symbol = VarSymbol(param_name, param_type)

            self.current_scope.insert(var_symbol)
            proc_symbol.params.append(var_symbol)

            formal_params.append(
                f'{param_name}{self.current_scope.scope_level} : {param_type.name}',
            )

        if node.params:
            result_str += '(' + '; '.join(formal_params) + ')'

        result_str = '\n'.join(
            '   ' + line
            for line in ((result_str + f';\n{self.visit(node.block_node)}; {{END OF {proc_name}}}').splitlines())
        )

        self.current_scope = self.current_scope.enclosing_scope

        return result_str

    def visit_VarDecl(self, node):
        type_name = node.type_node.value
        type_symbol = self.current_scope.lookup(type_name)
        type_scope_level = str(self.current_scope.lookup_scope_level(type_name))

        var_name = node.var_node.value
        var_symbol = VarSymbol(var_name, type_symbol)

        if self.current_scope.lookup(var_name, current_scope_only=True):
            raise Exception("Error: Duplicate identifier '%s' found" % var_name)

        self.current_scope.insert(var_symbol)

        return f'   VAR <{var_name+str(self.current_scope.scope_level)}:{type_name+type_scope_level}>;'

    def visit_Assign(self, node):
        return f'{self.visit(node.left)} := {self.visit(node.right)}'

    def visit_Var(self, node):
        var_name = node.value
        var_symbol = self.current_scope.lookup(var_name)

        if var_symbol is None:
            raise Exception("Error: Symbol(identifier) not found '%s'" % var_name)

        return f'<{var_name+str(var_symbol.scope.scope_level)}:{var_symbol.type.name}>'
