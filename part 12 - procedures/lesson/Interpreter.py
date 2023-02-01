from NodeVisitor import NodeVisitor
from Parser import Parser
from Token import Token


class Interpreter(NodeVisitor):
    def __init__(self, text):
        self.parser = Parser(text)
        self.GLOBAL_SCOPE = {}

    def visit_Program(self, node):
        self.visit(node.block)

    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_VarDecl(self, node):
        # Do nothing
        pass

    def visit_Type(self, node):
        # Do nothing
        pass

    def visit_BinOp(self, node):
        if node.op.type == Token.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Token.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Token.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == Token.INTEGER_DIV:
            return self.visit(node.left) // self.visit(node.right)
        elif node.op.type == Token.FLOAT_DIV:
            return float(self.visit(node.left)) / float(self.visit(node.right))

    def visit_Num(self, node):
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == Token.PLUS:
            return +self.visit(node.expr)
        elif op == Token.MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        var_value = self.visit(node.right)
        self.GLOBAL_SCOPE[var_name] = var_value

    def visit_Var(self, node):
        var_name = node.value
        var_value = self.GLOBAL_SCOPE.get(var_name)
        return var_value

    def visit_NoOp(self, node):
        pass

    def visit_ProcedureDecl(self, node):
        pass

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        return self.visit(tree)
