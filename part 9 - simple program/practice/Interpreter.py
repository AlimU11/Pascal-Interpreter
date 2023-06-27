from Node import NodeVisitor
from Parser import Parser
from Token import RESERVED_KEYWORDS, Token


class Interpreter(NodeVisitor):
    GLOBAL_SCOPE = {}

    def __init__(self, text):
        self.parser = Parser(text)
        Interpreter.GLOBAL_SCOPE = {}

    def visit_binop(self, node):
        if node.op.type == Token.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Token.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Token.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == RESERVED_KEYWORDS['DIV'].type:
            return self.visit(node.left) // self.visit(node.right)
        else:
            raise Exception('Unknown binary operator')

    def visit_num(self, node):
        return node.value

    def visit_unaryop(self, node):
        op = node.op.type
        if op == Token.PLUS:
            return +self.visit(node.expr)
        elif op == Token.MINUS:
            return -self.visit(node.expr)
        else:
            raise Exception('Unknown unary operator')

    def visit_compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_assign(self, node):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    def visit_var(self, node):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val is None:
            raise Exception(f'NameError: name \'{var_name}\' is not defined')
        else:
            return val

    def visit_noop(self, node):
        pass

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''

        return self.visit(tree)
