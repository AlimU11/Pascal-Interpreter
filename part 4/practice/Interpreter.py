from Lexer import Lexer
from Token import Token


class Interpreter(object):
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Error parsing input')

    def compare(self, token_types):
        if self.current_token.type in token_types:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        """<factor> ::= <whitespace>* <number> <whitespace>*"""

        result = self.current_token
        self.compare([Token.INTEGER])

        return result.value

    def operator(self):
        """<op> ::= "*" | "/" | "+" | "-" """

        op = self.current_token
        self.compare([Token.MULTIPLY, Token.DIVIDE, Token.PLUS, Token.MINUS])

        return op

    def eval(self, left, op, right):
        """<eval> ::= <term> <op> <term>"""

        if op.type == Token.MULTIPLY:
            return left * right
        elif op.type == Token.DIVIDE:
            return left / right
        elif op.type == Token.PLUS:
            return left + right
        elif op.type == Token.MINUS:
            return left - right

    def expr(self):
        """<expression> ::= <term> { <op> <term> }*"""

        result = self.term()

        while self.current_token.type in [Token.MULTIPLY, Token.DIVIDE, Token.PLUS, Token.MINUS]:
            op = self.operator()
            right = self.term()
            result = self.eval(result, op, right)

        return int(result)
