class Token(object):
    PLUS, MINUS, MULTIPLY, DIVIDE = 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'
    INTEGER = 'INTEGER'
    WHITESPACE, EOF = 'WHITESPACE', 'EOF'

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value),
        )

    def __repr__(self):
        return self.__str__()
