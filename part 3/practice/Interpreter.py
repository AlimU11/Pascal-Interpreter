from Token import Token


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def integer(self):
        number = ''  # self.current_char

        while self.pos < len(self.text) and self.current_char.isdigit():
            number += self.current_char if self.current_char and self.current_char.isdigit() else ''
            self.next()

        return int(number)

    def next(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip(self):
        while self.current_char and self.current_char.isspace():
            self.next()

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """

        if self.pos > len(self.text) - 1:
            return Token(Token.EOF, None)

        if self.current_char.isdigit():
            return Token(Token.INTEGER, self.integer())

        if self.current_char == '*':
            self.next()
            return Token(Token.MULTIPLY, '*')

        if self.current_char == '/':
            self.next()
            return Token(Token.DIVIDE, '/')

        if self.current_char.isspace():
            self.skip()
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
        if op == '*':
            return left * right
        elif op == '/':
            return left / right

    def opt(self):
        """<opt> ::= <op> <term>"""

        op = self.current_token
        self.eval([Token.MULTIPLY, Token.DIVIDE])

        right = self.current_token
        self.eval([Token.INTEGER])

        return op, right

    def expr(self):
        """<expression> ::= <term> { <op> <term> }*"""

        self.current_token = self.get_next_token()

        result = self.current_token.value
        self.eval([Token.INTEGER])

        while self.current_token.type != Token.EOF:
            op, right = self.opt()
            result = self.op(result, op.value, right.value)

        return result
