from railroad import (
    Choice,
    Diagram,
    NonTerminal,
    OneOrMore,
    Optional,
    Sequence,
    Terminal,
    ZeroOrMore,
)

paths = [
    'part 3/lesson/diagram.svg',
    'part 3/practice/diagram.svg',
    'part 4/lesson/diagram.svg',
    'part 4/practice/diagram.svg',
    'part 5 - operators precedence/lesson/diagram1.svg',
    'part 5 - operators precedence/lesson/diagram2.svg',
    'part 5 - operators precedence/lesson/diagram3.svg',
    'part 5 - operators precedence/practice/diagram1.svg',
    'part 5 - operators precedence/practice/diagram2.svg',
    'part 5 - operators precedence/practice/diagram3.svg',
    'part 6/lesson/diagram1.svg',
    'part 6/lesson/diagram2.svg',
    'part 6/lesson/diagram3.svg',
    'part 7 - AST/lesson/diagram1.svg',
    'part 7 - AST/lesson/diagram2.svg',
    'part 7 - AST/lesson/diagram3.svg',
    'part 7 - AST/practice/diagram1.svg',
    'part 7 - AST/practice/diagram2.svg',
    'part 7 - AST/practice/diagram3.svg',
    'part 8 - unary operators/lesson/diagram1.svg',
    'part 8 - unary operators/lesson/diagram2.svg',
    'part 8 - unary operators/lesson/diagram3.svg',
    'part 9 - simple program/lesson/src/diagram1.svg',
    'part 9 - simple program/lesson/src/diagram2.svg',
    'part 9 - simple program/lesson/src/diagram3.svg',
    'part 9 - simple program/lesson/src/diagram4.svg',
    'part 9 - simple program/lesson/src/diagram5.svg',
    'part 9 - simple program/lesson/src/diagram6.svg',
    'part 9 - simple program/lesson/src/diagram7.svg',
    'part 9 - simple program/lesson/src/diagram8.svg',
    'part 9 - simple program/practice/src/diagram1.svg',
    'part 9 - simple program/practice/src/diagram2.svg',
    'part 9 - simple program/practice/src/diagram3.svg',
    'part 9 - simple program/practice/src/diagram4.svg',
    'part 9 - simple program/practice/src/diagram5.svg',
    'part 9 - simple program/practice/src/diagram6.svg',
    'part 9 - simple program/practice/src/diagram7.svg',
    'part 9 - simple program/practice/src/diagram8.svg',
    'part 9 - simple program/practice/src/diagram9.svg',
    'part 9 - simple program/practice/src/diagram10.svg',
    'part 10 - complete program/lesson/src/diagram1.svg',
    'part 10 - complete program/lesson/src/diagram2.svg',
    'part 10 - complete program/lesson/src/diagram3.svg',
    'part 10 - complete program/lesson/src/diagram4.svg',
    'part 10 - complete program/lesson/src/diagram5.svg',
    'part 10 - complete program/lesson/src/diagram6.svg',
    'part 10 - complete program/lesson/src/diagram7.svg',
    'part 10 - complete program/lesson/src/diagram8.svg',
    'part 10 - complete program/lesson/src/diagram9.svg',
    'part 10 - complete program/lesson/src/diagram10.svg',
    'part 10 - complete program/lesson/src/diagram11.svg',
    'part 10 - complete program/lesson/src/diagram12.svg',
    'part 10 - complete program/lesson/src/diagram13.svg',
    'part 10 - complete program/lesson/src/diagram14.svg',
    'part 11 - symbol tables/lesson/src/diagram1.svg',
    'part 11 - symbol tables/lesson/src/diagram2.svg',
    'part 11 - symbol tables/lesson/src/diagram3.svg',
    'part 11 - symbol tables/lesson/src/diagram4.svg',
    'part 11 - symbol tables/lesson/src/diagram5.svg',
    'part 11 - symbol tables/lesson/src/diagram6.svg',
    'part 11 - symbol tables/lesson/src/diagram7.svg',
    'part 11 - symbol tables/lesson/src/diagram8.svg',
    'part 11 - symbol tables/lesson/src/diagram9.svg',
    'part 11 - symbol tables/lesson/src/diagram10.svg',
    'part 11 - symbol tables/lesson/src/diagram11.svg',
    'part 11 - symbol tables/lesson/src/diagram12.svg',
    'part 11 - symbol tables/lesson/src/diagram13.svg',
    'part 11 - symbol tables/lesson/src/diagram14.svg',
    'part 12 - procedures/lesson/src/diagram1.svg',
    'part 12 - procedures/lesson/src/diagram2.svg',
    'part 12 - procedures/lesson/src/diagram3.svg',
    'part 12 - procedures/lesson/src/diagram4.svg',
    'part 12 - procedures/lesson/src/diagram5.svg',
    'part 12 - procedures/lesson/src/diagram6.svg',
    'part 12 - procedures/lesson/src/diagram7.svg',
    'part 12 - procedures/lesson/src/diagram8.svg',
    'part 12 - procedures/lesson/src/diagram9.svg',
    'part 12 - procedures/lesson/src/diagram10.svg',
    'part 12 - procedures/lesson/src/diagram11.svg',
    'part 12 - procedures/lesson/src/diagram12.svg',
    'part 12 - procedures/lesson/src/diagram13.svg',
    'part 12 - procedures/lesson/src/diagram14.svg',
    'part 13 - semantic analysis/lesson/src/diagram1.svg',
    'part 13 - semantic analysis/lesson/src/diagram2.svg',
    'part 13 - semantic analysis/lesson/src/diagram3.svg',
    'part 13 - semantic analysis/lesson/src/diagram4.svg',
    'part 13 - semantic analysis/lesson/src/diagram5.svg',
    'part 13 - semantic analysis/lesson/src/diagram6.svg',
    'part 13 - semantic analysis/lesson/src/diagram7.svg',
    'part 13 - semantic analysis/lesson/src/diagram8.svg',
    'part 13 - semantic analysis/lesson/src/diagram9.svg',
    'part 13 - semantic analysis/lesson/src/diagram10.svg',
    'part 13 - semantic analysis/lesson/src/diagram11.svg',
    'part 13 - semantic analysis/lesson/src/diagram12.svg',
    'part 13 - semantic analysis/lesson/src/diagram13.svg',
    'part 13 - semantic analysis/lesson/src/diagram14.svg',
]

diagrams = [
    # 'part 3/lesson/diagram.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('+'),
                    Terminal('-'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 3/practice/diagram.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 4/lesson/diagram.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 4/practice/diagram.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                    Terminal('+'),
                    Terminal('-'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 5 - operators precedence/lesson/diagram1.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('+'),
                    Terminal('-'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 5 - operators precedence/lesson/diagram2.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 5 - operators precedence/lesson/diagram3.svg',
    Diagram(
        NonTerminal('number'),
    ),
    # 'part 5 - operators precedence/practice/diagram1.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('+'),
                    Terminal('-'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 5 - operators precedence/practice/diagram2.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 5 - operators precedence/practice/diagram3.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('number'),
            Sequence(
                Terminal('('),
                NonTerminal('expr'),
                Terminal(')'),
            ),
        ),
    ),
    # 'part 6/lesson/diagram1.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('+'),
                    Terminal('-'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 6/lesson/diagram2.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 6/lesson/diagram3.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('integer'),
            Sequence(
                Terminal('('),
                NonTerminal('expr'),
                Terminal(')'),
            ),
        ),
    ),
    # 'part 7 - AST/lesson/diagram1.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('+'),
                    Terminal('-'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 7 - AST/lesson/diagram2.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 7 - AST/lesson/diagram3.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('integer'),
            Sequence(
                Terminal('('),
                NonTerminal('expr'),
                Terminal(')'),
            ),
        ),
    ),
    # 'part 7 - AST/practice/diagram1.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('+'),
                    Terminal('-'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 7 - AST/practice/diagram2.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('*'),
                    Terminal('/'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 7 - AST/practice/diagram3.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('integer'),
            Sequence(
                Terminal('('),
                NonTerminal('expr'),
                Terminal(')'),
            ),
        ),
    ),
    # 'part 8 - unary operators/lesson/diagram1.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('plus'),
                    Terminal('minus'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 8 - unary operators/lesson/diagram2.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('mul'),
                    Terminal('div'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 8 - unary operators/lesson/diagram3.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Optional(
                    Choice(
                        0,
                        Terminal('plus'),
                        Terminal('minus'),
                    ),
                ),
                NonTerminal('factor'),
            ),
            NonTerminal('integer'),
            Sequence(
                Terminal('lparen'),
                NonTerminal('expr'),
                Terminal('rparen'),
            ),
        ),
    ),
    # 'part 9 - simple program/lesson/src/diagram1.svg',
    Diagram(
        NonTerminal('compound_statement'),
        Terminal('dot'),
    ),
    # 'part 9 - simple program/lesson/src/diagram2.svg',
    Diagram(
        Terminal('begin'),
        NonTerminal('statement_list'),
        Terminal('end'),
    ),
    # 'part 9 - simple program/lesson/src/diagram3.svg',
    Diagram(
        NonTerminal('statement'),
        ZeroOrMore(
            Terminal('semicolon'),
            NonTerminal('statement_list'),
        ),
    ),
    # 'part 9 - simple program/lesson/src/diagram4.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('compound_statement'),
            NonTerminal('assignment_statement'),
            NonTerminal('empty'),
        ),
    ),
    # 'part 9 - simple program/lesson/src/diagram5.svg',
    Diagram(
        NonTerminal('variable'),
        Terminal('assign'),
        NonTerminal('expr'),
    ),
    # 'part 9 - simple program/lesson/src/diagram6.svg',
    Diagram(
        Terminal('id'),
    ),
    # 'part 9 - simple program/lesson/src/diagram7.svg',
    Diagram(
        NonTerminal(''),
    ),
    # 'part 9 - simple program/lesson/src/diagram8.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('plus'),
                NonTerminal('factor'),
            ),
            Sequence(
                Terminal('minus'),
                NonTerminal('factor'),
            ),
            NonTerminal('integer'),
            Sequence(
                Terminal('lparen'),
                NonTerminal('expression'),
                Terminal('rparen'),
            ),
            NonTerminal('variable'),
        ),
    ),
    # 'part 9 - simple program/practice/src/diagram1.svg',
    Diagram(
        NonTerminal('compound_statement'),
        Terminal('dot'),
    ),
    # 'part 9 - simple program/practice/src/diagram2.svg',
    Diagram(
        Terminal('begin'),
        NonTerminal('statement_list'),
        Terminal('end'),
    ),
    # 'part 9 - simple program/practice/src/diagram3.svg',
    Diagram(
        NonTerminal('statement'),
        ZeroOrMore(
            Terminal('semicolon'),
            NonTerminal('statement_list'),
        ),
    ),
    # 'part 9 - simple program/practice/src/diagram4.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('compound_statement'),
            NonTerminal('assignment_statement'),
            NonTerminal('empty'),
        ),
    ),
    # 'part 9 - simple program/practice/src/diagram5.svg',
    Diagram(
        NonTerminal('variable'),
        Terminal('assign'),
        NonTerminal('expr'),
    ),
    # 'part 9 - simple program/practice/src/diagram6.svg',
    Diagram(
        Terminal('id'),
    ),
    # 'part 9 - simple program/practice/src/diagram7.svg',
    Diagram(
        NonTerminal(''),
    ),
    # 'part 9 - simple program/practice/src/diagram8.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('plus'),
                NonTerminal('factor'),
            ),
            Sequence(
                Terminal('minus'),
                NonTerminal('factor'),
            ),
            NonTerminal('integer'),
            Sequence(
                Terminal('lparen'),
                NonTerminal('expression'),
                Terminal('rparen'),
            ),
            NonTerminal('variable'),
        ),
    ),
    # 'part 9 - simple program/practice/src/diagram9.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('plus'),
                    Terminal('minus'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 9 - simple program/practice/src/diagram10.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('mul'),
                    Terminal('div'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 10 - complete program/lesson/src/diagram1.svg',
    Diagram(
        Terminal('PROGRAM'),
        NonTerminal('variable'),
        Terminal('SEMI'),
        NonTerminal('block'),
        Terminal('DOT'),
    ),
    # 'part 10 - complete program/lesson/src/diagram2.svg',
    Diagram(
        NonTerminal('declarations'),
        NonTerminal('compound_statement'),
    ),
    # 'part 10 - complete program/lesson/src/diagram3.svg',
    Diagram(
        Optional(
            Sequence(
                Terminal('VAR'),
                OneOrMore(
                    Sequence(
                        NonTerminal('variable_declaration'),
                        Terminal('SEMI'),
                    ),
                ),
            ),
        ),
    ),
    # 'part 10 - complete program/lesson/src/diagram4.svg',
    Diagram(
        Terminal('ID'),
        ZeroOrMore(
            Sequence(
                Terminal('COMMA'),
                Terminal('ID'),
            ),
        ),
        Terminal('COLON'),
        NonTerminal('type_spec'),
    ),
    # 'part 10 - complete program/lesson/src/diagram5.svg',
    Diagram(
        Choice(
            0,
            Terminal('INTEGER_TYPE'),
            Terminal('REAL_TYPE'),
        ),
    ),
    # 'part 10 - complete program/lesson/src/diagram6.svg',
    Diagram(
        Terminal('BEGIN'),
        NonTerminal('statement_list'),
        Terminal('END'),
    ),
    # 'part 10 - complete program/lesson/src/diagram7.svg',
    Diagram(
        NonTerminal('statement'),
        ZeroOrMore(
            Sequence(
                Terminal('SEMI'),
                NonTerminal('statement_list'),
            ),
        ),
    ),
    # 'part 10 - complete program/lesson/src/diagram8.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('compound_statement'),
            NonTerminal('assignment_statement'),
            NonTerminal('empty'),
        ),
    ),
    # 'part 10 - complete program/lesson/src/diagram9.svg',
    Diagram(
        NonTerminal('variable'),
        Terminal('ASSIGN'),
        NonTerminal('expression'),
    ),
    # 'part 10 - complete program/lesson/src/diagram10.svg',
    Diagram(
        Terminal(' '),
    ),
    # 'part 10 - complete program/lesson/src/diagram11.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('PLUS'),
                    Terminal('MINUS'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 10 - complete program/lesson/src/diagram12.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('MUL'),
                    Terminal('INTEGER_DIV'),
                    Terminal('FLOAT_DIV'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 10 - complete program/practice/src/diagram13.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('PLUS'),
                NonTerminal('factor'),
            ),
            Sequence(
                Terminal('MINUS'),
                NonTerminal('factor'),
            ),
            NonTerminal('INTEGER'),
            NonTerminal('REAL'),
            Sequence(
                Terminal('LPAREN'),
                NonTerminal('expression'),
                Terminal('RPAREN'),
            ),
            NonTerminal('variable'),
        ),
    ),
    # 'part 10 - complete program/practice/src/diagram14.svg',
    Diagram(
        Terminal('ID'),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram1.svg',
    Diagram(
        Terminal('PROGRAM'),
        NonTerminal('variable'),
        Terminal('SEMI'),
        NonTerminal('block'),
        Terminal('DOT'),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram2.svg',
    Diagram(
        NonTerminal('declarations'),
        NonTerminal('compound_statement'),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram3.svg',
    Diagram(
        Optional(
            Sequence(
                Terminal('VAR'),
                OneOrMore(
                    Sequence(
                        NonTerminal('variable_declaration'),
                        Terminal('SEMI'),
                    ),
                ),
            ),
        ),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram4.svg',
    Diagram(
        Terminal('ID'),
        ZeroOrMore(
            Sequence(
                Terminal('COMMA'),
                Terminal('ID'),
            ),
        ),
        Terminal('COLON'),
        NonTerminal('type_spec'),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram5.svg',
    Diagram(
        Choice(
            0,
            Terminal('INTEGER_TYPE'),
            Terminal('REAL_TYPE'),
        ),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram6.svg',
    Diagram(
        Terminal('BEGIN'),
        NonTerminal('statement_list'),
        Terminal('END'),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram7.svg',
    Diagram(
        NonTerminal('statement'),
        ZeroOrMore(
            Sequence(
                Terminal('SEMI'),
                NonTerminal('statement_list'),
            ),
        ),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram8.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('compound_statement'),
            NonTerminal('assignment_statement'),
            NonTerminal('empty'),
        ),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram9.svg',
    Diagram(
        NonTerminal('variable'),
        Terminal('ASSIGN'),
        NonTerminal('expression'),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram10.svg',
    Diagram(
        Terminal(' '),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram11.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('PLUS'),
                    Terminal('MINUS'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 11 - symbol tables/lesson/src/diagram12.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('MUL'),
                    Terminal('INTEGER_DIV'),
                    Terminal('FLOAT_DIV'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 11 - symbol tables/practice/src/diagram13.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('PLUS'),
                NonTerminal('factor'),
            ),
            Sequence(
                Terminal('MINUS'),
                NonTerminal('factor'),
            ),
            NonTerminal('INTEGER'),
            NonTerminal('REAL'),
            Sequence(
                Terminal('LPAREN'),
                NonTerminal('expression'),
                Terminal('RPAREN'),
            ),
            NonTerminal('variable'),
        ),
    ),
    # 'part 11 - symbol tables/practice/src/diagram14.svg',
    Diagram(
        Terminal('ID'),
    ),
    # 'part 12 - procedures/lesson/src/diagram1.svg',
    Diagram(
        Terminal('PROGRAM'),
        NonTerminal('variable'),
        Terminal('SEMI'),
        NonTerminal('block'),
        Terminal('DOT'),
    ),
    # 'part 12 - procedures/lesson/src/diagram2.svg',
    Diagram(
        NonTerminal('declarations'),
        NonTerminal('compound_statement'),
    ),
    # 'part 12 - procedures/lesson/src/diagram3.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('VAR'),
                OneOrMore(
                    Sequence(
                        NonTerminal('variable_declaration'),
                        Terminal('SEMI'),
                    ),
                ),
            ),
            Sequence(
                ZeroOrMore(
                    Sequence(
                        Terminal('PROCEDURE'),
                        Terminal('ID'),
                        Terminal('SEMI'),
                        NonTerminal('block'),
                        Terminal('SEMI'),
                    ),
                ),
            ),
            NonTerminal('empty'),
        ),
    ),
    # 'part 12 - procedures/lesson/src/diagram4.svg',
    Diagram(
        Terminal('ID'),
        ZeroOrMore(
            Sequence(
                Terminal('COMMA'),
                Terminal('ID'),
            ),
        ),
        Terminal('COLON'),
        NonTerminal('type_spec'),
    ),
    # 'part 12 - procedures/lesson/src/diagram5.svg',
    Diagram(
        Choice(
            0,
            Terminal('INTEGER_TYPE'),
            Terminal('REAL_TYPE'),
        ),
    ),
    # 'part 12 - procedures/lesson/src/diagram6.svg',
    Diagram(
        Terminal('BEGIN'),
        NonTerminal('statement_list'),
        Terminal('END'),
    ),
    # 'part 12 - procedures/lesson/src/diagram7.svg',
    Diagram(
        NonTerminal('statement'),
        ZeroOrMore(
            Sequence(
                Terminal('SEMI'),
                NonTerminal('statement_list'),
            ),
        ),
    ),
    # 'part 12 - procedures/lesson/src/diagram8.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('compound_statement'),
            NonTerminal('assignment_statement'),
            NonTerminal('empty'),
        ),
    ),
    # 'part 12 - procedures/lesson/src/diagram9.svg',
    Diagram(
        NonTerminal('variable'),
        Terminal('ASSIGN'),
        NonTerminal('expression'),
    ),
    # 'part 12 - procedures/lesson/src/diagram10.svg',
    Diagram(
        Terminal(' '),
    ),
    # 'part 12 - procedures/lesson/src/diagram11.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('PLUS'),
                    Terminal('MINUS'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 12 - procedures/lesson/src/diagram12.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('MUL'),
                    Terminal('INTEGER_DIV'),
                    Terminal('FLOAT_DIV'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 12 - procedures/practice/src/diagram13.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('PLUS'),
                NonTerminal('factor'),
            ),
            Sequence(
                Terminal('MINUS'),
                NonTerminal('factor'),
            ),
            NonTerminal('INTEGER'),
            NonTerminal('REAL'),
            Sequence(
                Terminal('LPAREN'),
                NonTerminal('expression'),
                Terminal('RPAREN'),
            ),
            NonTerminal('variable'),
        ),
    ),
    # 'part 12 - procedures/practice/src/diagram14.svg',
    Diagram(
        Terminal('ID'),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram1.svg',
    Diagram(
        Terminal('PROGRAM'),
        NonTerminal('variable'),
        Terminal('SEMI'),
        NonTerminal('block'),
        Terminal('DOT'),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram2.svg',
    Diagram(
        NonTerminal('declarations'),
        NonTerminal('compound_statement'),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram3.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('VAR'),
                OneOrMore(
                    Sequence(
                        NonTerminal('variable_declaration'),
                        Terminal('SEMI'),
                    ),
                ),
            ),
            Sequence(
                ZeroOrMore(
                    Sequence(
                        Terminal('PROCEDURE'),
                        Terminal('ID'),
                        Terminal('SEMI'),
                        NonTerminal('block'),
                        Terminal('SEMI'),
                    ),
                ),
            ),
            NonTerminal('empty'),
        ),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram4.svg',
    Diagram(
        Terminal('ID'),
        ZeroOrMore(
            Sequence(
                Terminal('COMMA'),
                Terminal('ID'),
            ),
        ),
        Terminal('COLON'),
        NonTerminal('type_spec'),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram5.svg',
    Diagram(
        Choice(
            0,
            Terminal('INTEGER_TYPE'),
            Terminal('REAL_TYPE'),
        ),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram6.svg',
    Diagram(
        Terminal('BEGIN'),
        NonTerminal('statement_list'),
        Terminal('END'),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram7.svg',
    Diagram(
        NonTerminal('statement'),
        ZeroOrMore(
            Sequence(
                Terminal('SEMI'),
                NonTerminal('statement_list'),
            ),
        ),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram8.svg',
    Diagram(
        Choice(
            0,
            NonTerminal('compound_statement'),
            NonTerminal('assignment_statement'),
            NonTerminal('empty'),
        ),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram9.svg',
    Diagram(
        NonTerminal('variable'),
        Terminal('ASSIGN'),
        NonTerminal('expression'),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram10.svg',
    Diagram(
        Terminal(' '),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram11.svg',
    Diagram(
        NonTerminal('term'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('PLUS'),
                    Terminal('MINUS'),
                ),
                NonTerminal('term'),
            ),
        ),
    ),
    # 'part 13 - semantic analysis/lesson/src/diagram12.svg',
    Diagram(
        NonTerminal('factor'),
        ZeroOrMore(
            Sequence(
                Choice(
                    0,
                    Terminal('MUL'),
                    Terminal('INTEGER_DIV'),
                    Terminal('FLOAT_DIV'),
                ),
                NonTerminal('factor'),
            ),
        ),
    ),
    # 'part 13 - semantic analysis/practice/src/diagram13.svg',
    Diagram(
        Choice(
            0,
            Sequence(
                Terminal('PLUS'),
                NonTerminal('factor'),
            ),
            Sequence(
                Terminal('MINUS'),
                NonTerminal('factor'),
            ),
            NonTerminal('INTEGER'),
            NonTerminal('REAL'),
            Sequence(
                Terminal('LPAREN'),
                NonTerminal('expression'),
                Terminal('RPAREN'),
            ),
            NonTerminal('variable'),
        ),
    ),
    # 'part 13 - semantic analysis/practice/src/diagram14.svg',
    Diagram(
        Terminal('ID'),
    ),
]


if __name__ == '__main__':
    for path, diagram in zip(paths, diagrams):
        diagram.writeSvg(open(path, 'w').write)
