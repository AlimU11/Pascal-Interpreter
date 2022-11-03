from AST import Assign, BinOp, Compound, NoOp, Num, UnaryOp, Var
from Lexer import Lexer
from Token import RESERVED_KEYWORDS, Token


class Parser(object):
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = self.lexer.get_next_token()

    def error(self, message=None):
        raise Exception(f'SyntaxError: ' + ('\nError near \'' + message + '\'' if message else ''))

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(self.current_token)

    def program(self):
        """program : compound_statement DOT"""
        node = self.compound_statement()
        self.eat(Token.DOT)
        return node

    def compound_statement(self):
        """compound_statement: BEGIN statement_list END"""
        self.eat(Token.BEGIN)
        nodes = self.statement_list()
        self.eat(Token.END)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def statement_list(self):
        """statement_list : statement
        | statement SEMI statement_list
        """
        node = self.statement()

        results = [node]

        while self.current_token.type == Token.SEMI:
            self.eat(Token.SEMI)
            results.append(self.statement())

        if self.current_token.type == Token.ID:
            self.error()

        return results

    def statement(self):
        """statement : compound_statement
        | assignment_statement
        | empty
        """
        if self.current_token.type == Token.BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == Token.ID:
            node = self.assignment_statement()
        else:
            node = self.empty()
        return node

    def assignment_statement(self):
        """assignment_statement : variable ASSIGN expr"""
        left = self.variable()
        token = self.current_token
        self.eat(Token.ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def variable(self):
        """variable : ID"""
        node = Var(self.current_token)
        self.eat(Token.ID)
        return node

    def empty(self):
        """An empty production"""
        return NoOp()

    def expr(self):
        """expr : term ((PLUS | MINUS) term)*"""
        node = self.term()

        while self.current_token.type in (Token.PLUS, Token.MINUS):
            token = self.current_token
            if token.type == Token.PLUS:
                self.eat(Token.PLUS)
            elif token.type == Token.MINUS:
                self.eat(Token.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (Token.MUL, RESERVED_KEYWORDS['DIV'].type):
            token = self.current_token
            if token.type == Token.MUL:
                self.eat(Token.MUL)
            elif token.type == RESERVED_KEYWORDS['DIV'].type:
                self.eat(RESERVED_KEYWORDS['DIV'].type)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def factor(self):
        """factor : PLUS factor
        | MINUS factor
        | INTEGER
        | LPAREN expr RPAREN
        | variable
        """
        token = self.current_token
        if token.type == Token.PLUS:
            self.eat(Token.PLUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == Token.MINUS:
            self.eat(Token.MINUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == Token.INTEGER:
            self.eat(Token.INTEGER)
            return Num(token)
        elif token.type == Token.LPAREN:
            self.eat(Token.LPAREN)
            node = self.expr()
            self.eat(Token.RPAREN)
            return node
        else:
            node = self.variable()
            return node

    def parse(self):
        """
        program : compound_statement DOT
        compound_statement : BEGIN statement_list END
        statement_list : statement
                       | statement SEMI statement_list
        statement : compound_statement
                  | assignment_statement
                  | empty
        assignment_statement : variable ASSIGN expr
        empty :
        expression: term ((PLUS | MINUS) term)*
        term: factor ((MUL | DIV) factor)*
        factor : PLUS factor
               | MINUS factor
               | INTEGER
               | LPAREN expression RPAREN
               | variable
        variable: ID
        """
        node = self.program()
        if self.current_token.type != Token.EOF:
            self.error('Unexpected EOF While Parsing')

        return node
