from Token import Token


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(Token.EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        if current_char.isdigit():
            number = current_char

            while self.pos < len(text) - 1 and current_char.isdigit():
                self.pos += 1
                current_char = text[self.pos]
                number += current_char if current_char.isdigit() else ''

            token = Token(Token.INTEGER, int(number))
            return token

        if current_char == '+':
            token = Token(Token.PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(Token.MINUS, current_char)
            self.pos += 1
            return token

        if current_char == ' ':
            token = Token(Token.WHITESPACE, current_char)
            self.pos += 1
            return self.get_next_token()

        self.error()

    def eval(self, token_types):
        """compare the current token type with the passed token family"""

        if self.current_token.type in token_types:
            self.current_token = self.get_next_token()

        else:
            self.error()

    def op(self, left, op, right):
        """Arithmetic operator dispatcher."""
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def expr(self):
        """<expression> ::= <term> <op> <term>"""

        self.current_token = self.get_next_token()

        left = self.current_token
        self.eval([Token.INTEGER])

        op = self.current_token
        self.eval([Token.PLUS, Token.MINUS])

        right = self.current_token
        self.eval([Token.INTEGER])

        result = self.op(left.value, op.value, right.value)
        return result
