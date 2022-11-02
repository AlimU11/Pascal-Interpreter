from Node import NodeVisitor
from Parser import Parser
from Token import Token


class Interpreter(NodeVisitor):
    def __init__(self, text):
        self.parser = Parser(text)

    def visit_BinOp(self, node):
        if node.op.type == Token.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Token.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Token.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == Token.DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == Token.PLUS:
            return +self.visit(node.expr)
        elif op == Token.MINUS:
            return -self.visit(node.expr)

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

    def expr(self):
        return self.interpret()
