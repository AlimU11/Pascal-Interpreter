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

    def factor(self):
        """<factor> ::= <number> | "(" <expression> ")" """
        if self.current_token.type == Token.INTEGER:
            result = self.current_token.value
            self.compare([Token.INTEGER])
        elif self.current_token.type == Token.LEFTPARENTHESIS:
            self.compare([Token.LEFTPARENTHESIS])
            result = self.expr()
            self.compare([Token.RIGHTPARENTHESIS])
        else:
            result = None
            self.error()

        return result

    def term(self):
        """<term> ::= <factor> { ("*" | "/") <factor> }*"""
        result = self.factor()

        while self.current_token.type in [Token.MULTIPLY, Token.DIVIDE]:
            op = self.current_token
            self.compare([Token.MULTIPLY, Token.DIVIDE])

            right = self.factor()

            result = self.eval(result, op, right)

        return result

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
        """<expression> ::= <term> { ("+" | "-") <term> }*"""

        result = self.term()

        while self.current_token.type in [Token.PLUS, Token.MINUS]:
            op = self.current_token
            self.compare([Token.PLUS, Token.MINUS])

            right = self.term()

            result = self.eval(result, op, right)

        return int(result)
