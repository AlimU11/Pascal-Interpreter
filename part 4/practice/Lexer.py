from Token import Token


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def integer(self):
        number = ''

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

        if self.current_char == '+':
            self.next()
            return Token(Token.PLUS, '+')

        if self.current_char == '-':
            self.next()
            return Token(Token.MINUS, '-')

        if self.current_char.isspace():
            self.skip()
            return self.get_next_token()

        self.error()
