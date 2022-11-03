class Token(object):
    (INTEGER, PLUS, MINUS, MUL, LPAREN, RPAREN, ID, ASSIGN, BEGIN, END, SEMI, DOT, EOF) = (
        'INTEGER',
        'PLUS',
        'MINUS',
        'MUL',
        '(',
        ')',
        'ID',
        'ASSIGN',
        'BEGIN',
        'END',
        'SEMI',
        'DOT',
        'EOF',
    )

    def __init__(self, type, value):
        self.type = type
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


RESERVED_KEYWORDS = {
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END'),
    'DIV': Token('DIV', 'DIV'),
}
