class Token(object):
    # Token types
    #
    # EOF (end-of-file) token is used to indicate that
    # there is no more input left for lexical analysis
    INTEGER, MUL, DIV, EOF = 'INTEGER', 'MUL', 'DIV', 'EOF'

    def __init__(self, type, value):
        # token type: INTEGER, MUL, DIV, or EOF
        self.type = type
        # token value: non-negative integer value, '*', '/', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value),
        )

    def __repr__(self):
        return self.__str__()
