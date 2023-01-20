from AST import (
    Assign,
    BinOp,
    Block,
    Compound,
    NoOp,
    Num,
    Program,
    Type,
    UnaryOp,
    Var,
    VarDecl,
)
from Lexer import Lexer
from Token import RESERVED_KEYWORDS, Token


class Parser(object):
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def program(self):
        self.eat(Token.PROGRAM)
        var_node = self.variable()
        prog_name = var_node.value
        self.eat(Token.SEMI)
        block_node = self.block()
        program_node = Program(prog_name, block_node)
        self.eat(Token.DOT)
        return program_node

    def block(self):
        declaration_nodes = self.declarations()
        compound_statement_node = self.compound_statement()
        node = Block(declaration_nodes, compound_statement_node)
        return node

    def declarations(self):
        declarations = []
        if self.current_token.type == Token.VAR:
            self.eat(Token.VAR)
            while self.current_token.type == Token.ID:
                var_decl = self.variable_declaration()
                declarations.extend(var_decl)
                self.eat(Token.SEMI)

        return declarations

    def variable_declaration(self):
        var_nodes = [Var(self.current_token)]  # first ID
        self.eat(Token.ID)

        while self.current_token.type == Token.COMMA:
            self.eat(Token.COMMA)
            var_nodes.append(Var(self.current_token))
            self.eat(Token.ID)

        self.eat(Token.COLON)

        type_node = self.type_spec()
        var_declarations = [VarDecl(var_node, type_node) for var_node in var_nodes]
        return var_declarations

    def type_spec(self):
        token = self.current_token
        if self.current_token.type == Token.INTEGER_TYPE:
            self.eat(Token.INTEGER_TYPE)
        else:
            self.eat(Token.REAL_TYPE)
        node = Type(token)
        return node

    def compound_statement(self):
        self.eat(Token.BEGIN)
        nodes = self.statement_list()
        self.eat(Token.END)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def statement_list(self):
        node = self.statement()

        results = [node]

        while self.current_token.type == Token.SEMI:
            self.eat(Token.SEMI)
            results.append(self.statement())

        return results

    def statement(self):
        if self.current_token.type == Token.BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == Token.ID:
            node = self.assignment_statement()
        else:
            node = self.empty()
        return node

    def assignment_statement(self):
        left = self.variable()
        token = self.current_token
        self.eat(Token.ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def variable(self):
        node = Var(self.current_token)
        self.eat(Token.ID)
        return node

    def empty(self):
        return NoOp()

    def expr(self):
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
        node = self.factor()

        while self.current_token.type in (Token.MUL, Token.INTEGER_DIV, Token.FLOAT_DIV):
            token = self.current_token
            if token.type == Token.MUL:
                self.eat(Token.MUL)
            elif token.type == Token.INTEGER_DIV:
                self.eat(Token.INTEGER_DIV)
            elif token.type == Token.FLOAT_DIV:
                self.eat(Token.FLOAT_DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def factor(self):
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
        elif token.type == Token.REAL:
            self.eat(Token.REAL)
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
        node = self.program()
        if self.current_token.type != Token.EOF:
            self.error()

        return node
