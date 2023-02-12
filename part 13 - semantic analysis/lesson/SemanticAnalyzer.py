from NodeVisitor import NodeVisitor
from Parser import Parser
from Symbol import VarSymbol
from SymbolTable import SymbolTable


class SemanticAnalyzer(NodeVisitor):
    def __init__(self, text):
        self.parser = Parser(text)
        self.symbol_table = SymbolTable()

    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_Program(self, node):
        self.visit(node.block)

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
        type_symbol = self.symbol_table.lookup(type_name)
        var_name = node.var_node.value
        var_symbol = VarSymbol(var_name, type_symbol)

        if self.symbol_table.lookup(var_name) is not None:
            raise Exception(
                "Error: Duplicate identifier '%s' found" % var_name,
            )

        self.symbol_table.define(var_symbol)

    def visit_Assign(self, node):
        var_name = node.left.value
        var_symbol = self.symbol_table.lookup(var_name)

        if var_symbol is None:
            raise NameError(repr(var_name))

        self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        var_symbol = self.symbol_table.lookup(var_name)

        if var_symbol is None:
            raise NameError(repr(var_name))

    def visit_ProcedureDecl(self, node):
        pass

    def analyze(self):
        return self.visit(self.parser.parse())
