from railroad import (
    Choice,
    Diagram,
    NonTerminal,
    Optional,
    Sequence,
    Terminal,
    ZeroOrMore,
)

paths = [
    '../part 3/lesson/diagram.svg',
    '../part 3/practice/diagram.svg',
    '../part 4/lesson/diagram.svg',
    '../part 4/practice/diagram.svg',
    '../part 5 - operators precedence/lesson/diagram1.svg',
    '../part 5 - operators precedence/lesson/diagram2.svg',
    '../part 5 - operators precedence/lesson/diagram3.svg',
    '../part 5 - operators precedence/practice/diagram1.svg',
    '../part 5 - operators precedence/practice/diagram2.svg',
    '../part 5 - operators precedence/practice/diagram3.svg',
    '../part 6/lesson/diagram1.svg',
    '../part 6/lesson/diagram2.svg',
    '../part 6/lesson/diagram3.svg',
    '../part 7 - AST/lesson/diagram1.svg',
    '../part 7 - AST/lesson/diagram2.svg',
    '../part 7 - AST/lesson/diagram3.svg',
    '../part 7 - AST/practice/diagram1.svg',
    '../part 7 - AST/practice/diagram2.svg',
    '../part 7 - AST/practice/diagram3.svg',
    '../part 8 - unary operators/lesson/diagram1.svg',
    '../part 8 - unary operators/lesson/diagram2.svg',
    '../part 8 - unary operators/lesson/diagram3.svg',
]

diagrams = [
    # '../part 3/lesson/diagram.svg',
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
    # '../part 3/practice/diagram.svg',
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
    # '../part 4/lesson/diagram.svg',
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
    # '../part 4/practice/diagram.svg',
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
    # '../part 5 - operators precedence/lesson/diagram1.svg',
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
    # '../part 5 - operators precedence/lesson/diagram2.svg',
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
    # '../part 5 - operators precedence/lesson/diagram3.svg',
    Diagram(
        NonTerminal('number'),
    ),
    # '../part 5 - operators precedence/practice/diagram1.svg',
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
    # '../part 5 - operators precedence/practice/diagram2.svg',
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
    # '../part 5 - operators precedence/practice/diagram3.svg',
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
    # '../part 6/lesson/diagram1.svg',
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
    # '../part 6/lesson/diagram2.svg',
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
    # '../part 6/lesson/diagram3.svg',
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
    # '../part 7 - AST/lesson/diagram1.svg',
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
    # '../part 7 - AST/lesson/diagram2.svg',
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
    # '../part 7 - AST/lesson/diagram3.svg',
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
    # '../part 7 - AST/practice/diagram1.svg',
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
    # '../part 7 - AST/practice/diagram2.svg',
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
    # '../part 7 - AST/practice/diagram3.svg',
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
    # '../part 8 - unary operators/lesson/diagram1.svg',
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
    # '../part 8 - unary operators/lesson/diagram2.svg',
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
    # '../part 8 - unary operators/lesson/diagram3.svg',
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
]


if __name__ == '__main__':
    for path, diagram in zip(paths, diagrams):
        diagram.writeSvg(open(path, 'w').write)
