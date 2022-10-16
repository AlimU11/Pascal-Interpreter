class Token(object):
    INTEGER, PLUS, MINUS, MUL, DIV, EOF = (
        'INTEGER',
        'PLUS',
        'MINUS',
        'MUL',
        'DIV',
        'EOF',
    )

    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, MUL, DIV, or EOF
        self.type = type
        # token value: non-negative integer value, '+', '-', '*', '/', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value),
        )

    def __repr__(self):
        return self.__str__()
