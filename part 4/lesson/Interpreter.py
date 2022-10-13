from Lexer import Lexer
from Token import Token


class Interpreter(object):
    def __init__(self, text):
        self.lexer = Lexer(text)
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """Return an INTEGER token value.

        factor : INTEGER
        """
        token = self.current_token
        self.eat(Token.INTEGER)
        return token.value

    def expr(self):
        """Arithmetic expression parser / interpreter.

        expr   : factor ((MUL | DIV) factor)*
        factor : INTEGER
        """
        result = self.factor()

        while self.current_token.type in (Token.MUL, Token.DIV):
            token = self.current_token
            if token.type == Token.MUL:
                self.eat(Token.MUL)
                result = result * self.factor()
            elif token.type == Token.DIV:
                self.eat(Token.DIV)
                result = result / self.factor()

        return result
