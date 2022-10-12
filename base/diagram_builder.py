from railroad import Choice, Diagram, NonTerminal, Sequence, Terminal, ZeroOrMore

paths = [
    '../part 3/lesson/diagram.svg',
    '../part 3/practice/diagram.svg',
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
]


if __name__ == '__main__':
    for path, diagram in zip(paths, diagrams):
        diagram.writeSvg(open(path, 'w').write)
