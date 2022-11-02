from Node import NodeVisitor
from Parser import Parser
from PostfixTranslator import PostfixTranslator
from PrefixTranslator import PrefixTranslator
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

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

    def expr(self):
        tree = self.parser.parse()
        postfix_translator = PostfixTranslator(tree)
        postfix_translation = postfix_translator.translate()

        prefix_translator = PrefixTranslator(tree)
        prefix_translation = prefix_translator.translate()

        return ' '.join([str(i) for i in postfix_translation]) + ' | ' + ' '.join([str(i) for i in prefix_translation])
