from AST import (
    Assign,
    BinOp,
    Block,
    Compound,
    NoOp,
    Num,
    ProcedureDecl,
    Program,
    Type,
    UnaryOp,
    Var,
    VarDecl,
)
from Lexer import Lexer
from Token import Token


class Parser(object):
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def program(self):
        """program : PROGRAM variable SEMI block DOT"""
        self.eat(Token.PROGRAM)
        var_node = self.variable()
        prog_name = var_node.value
        self.eat(Token.SEMI)
        block_node = self.block()
        program_node = Program(prog_name, block_node)
        self.eat(Token.DOT)
        return program_node

    def block(self):
        """block : declarations compound_statement"""
        declaration_nodes = self.declarations()
        compound_statement_node = self.compound_statement()
        node = Block(declaration_nodes, compound_statement_node)
        return node

    def declarations(self):
        """declarations : VAR { variable_declaration SEMI }+
        | { PROCEDURE ID SEMI block SEMI }*
        | empty
        """
        declarations = []

        if self.current_token.type == Token.VAR:
            self.eat(Token.VAR)
            while self.current_token.type == Token.ID:
                var_decl = self.variable_declaration()
                declarations.extend(var_decl)
                self.eat(Token.SEMI)

        while self.current_token.type == Token.PROCEDURE:
            self.eat(Token.PROCEDURE)
            proc_name = self.current_token.value
            self.eat(Token.ID)
            self.eat(Token.SEMI)
            block_node = self.block()
            proc_declaration = ProcedureDecl(proc_name, block_node)
            declarations.append(proc_declaration)
            self.eat(Token.SEMI)

        return declarations

    def variable_declaration(self):
        """variable_declaration : ID (COMMA ID)* COLON type_spec"""
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
        """type_spec : INTEGER
        | REAL
        """
        token = self.current_token
        if self.current_token.type == Token.INTEGER:
            self.eat(Token.INTEGER)
        else:
            self.eat(Token.REAL)
        node = Type(token)
        return node

    def compound_statement(self):
        """
        compound_statement: BEGIN statement_list END
        """
        self.eat(Token.BEGIN)
        nodes = self.statement_list()
        self.eat(Token.END)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def statement_list(self):
        """
        statement_list : statement
                       | statement SEMI statement_list
        """
        node = self.statement()

        results = [node]

        while self.current_token.type == Token.SEMI:
            self.eat(Token.SEMI)
            results.append(self.statement())

        return results

    def statement(self):
        """
        statement : compound_statement
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
        """
        assignment_statement : variable ASSIGN expr
        """
        left = self.variable()
        token = self.current_token
        self.eat(Token.ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def variable(self):
        """
        variable : ID
        """
        node = Var(self.current_token)
        self.eat(Token.ID)
        return node

    def empty(self):
        """An empty production"""
        return NoOp()

    def expr(self):
        """
        expr : term ((PLUS | MINUS) term)*
        """
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
        """term : factor ((MUL | INTEGER_DIV | FLOAT_DIV) factor)*"""
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
        """factor : PLUS factor
        | MINUS factor
        | INTEGER_CONST
        | REAL_CONST
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
        elif token.type == Token.INTEGER_CONST:
            self.eat(Token.INTEGER_CONST)
            return Num(token)
        elif token.type == Token.REAL_CONST:
            self.eat(Token.REAL_CONST)
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
