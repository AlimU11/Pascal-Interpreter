from base.Error import LexerError
from base.Token import Token
from base.TokenType import TokenType


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.lineno = 1
        self.column = 1

    def error(self):
        raise LexerError(
            message=f'Invalid character: "{self.current_char}" at line {self.lineno} column {self.column}',
        )

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        if self.current_char == '\n':
            self.lineno += 1
            self.column = 0

        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
            self.column += 1

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char != '}':
            self.advance()
        self.advance()

    def number(self):
        """Return a (multidigit) integer or float consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

            token = Token(TokenType.REAL_CONST, float(result), self.lineno, self.column)
        else:
            token = Token(
                TokenType.INTEGER_CONST,
                int(result),
                self.lineno,
                self.column,
            )

        return token

    def _id(self):
        """Handle identifiers and reserved keywords"""

        value = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            value += self.current_char
            self.advance()

        token_type = Token.RESERVED_KEYWORDS.get(value.upper(), TokenType.ID)

        token = Token(
            type=token_type,
            value=value.upper(),
            lineno=self.lineno,
            column=self.column,
        )

        return token

    def get_next_token(self) -> Token:
        """Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '{':
                self.advance()
                self.skip_comment()
                continue

            if self.current_char.isalpha() or self.current_char == '_':
                return self._id()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == ':' and self.peek() == '=':
                token = Token(
                    type=TokenType.ASSIGN,
                    value=TokenType.ASSIGN.value,
                    lineno=self.lineno,
                    column=self.column,
                )
                self.advance()
                self.advance()
                return token

            try:
                token_type = TokenType(self.current_char)
            except ValueError:
                self.error()
            else:
                token = Token(
                    type=token_type,
                    value=token_type.value,
                    lineno=self.lineno,
                    column=self.column,
                )
                self.advance()
                return token

        return Token(
            type=TokenType.EOF,
            value=None,
            lineno=self.lineno,
            column=self.column,
        )
