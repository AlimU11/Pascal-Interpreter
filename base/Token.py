from base.TokenType import TokenType


class Token(object):
    def __init__(self, type, value, lineno, column):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.column = column

    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return f'Token({self.type}, {repr(self.value)}), position: {self.lineno}:{self.column}'

    def __repr__(self):
        return self.__str__()

    def _build_reserved_keywords():
        tokens = list(TokenType)
        start_idx = tokens.index(TokenType.PROGRAM)
        end_idx = tokens.index(TokenType.WRITELN)

        return {token.value: token for token in tokens[start_idx : end_idx + 1]}

    def _build_reserved_procedures():
        tokens = list(TokenType)
        start_idx = tokens.index(TokenType.WRITELN)
        end_idx = tokens.index(TokenType.WRITELN)

        return {token.value: token for token in tokens[start_idx : end_idx + 1]}

    RESERVED_KEYWORDS = _build_reserved_keywords()
    RESERVED_PROCEDURES = _build_reserved_procedures()
