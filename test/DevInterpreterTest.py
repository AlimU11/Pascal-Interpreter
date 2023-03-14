import unittest

from TestMethods import TestMethods


class DevInterpreterTestCase(TestMethods):
    def test_part9_lesson(self):
        self.abstract_program_test('part 9 - simple program/lesson')

    def test_part9_practice(self):
        self.abstract_program_test('part 9 - simple program/practice')

    def test_part_10_lesson(self):
        self.abstract_program_test('part 10 - complete program/lesson')

    def test_part_11_lesson(self):
        self.abstract_program_test('part 11 - symbol tables/lesson')

    def test_part_12_lesson(self):
        self.abstract_program_test('part 12 - procedures/lesson')

    def test_part_13_lesson(self):
        self.abstract_test_fail('part 13 - semantic analysis/lesson')

    def test_part_14_practice(self):
        self.abstract_program_test('part 14 - nested scopes/practice', test_scopes=True)

    def test_part_15_lesson(self):
        self.abstract_test_fail(
            'part 15 - error processing/lesson',
            exception='SemanticError',
        )

    def test_part_16_lesson(self):
        self.abstract_test_pass('part 16 - recognizing procedure calls/lesson')

    def test_part_16_practice(self):
        self.abstract_test_fail('part 16 - recognizing procedure calls/practice')

    def test_part_17_lesson(self):
        path = 'part 17 - call stack and activation records/lesson'

        self.import_modules(path)
        src_program = TestMethods.base + 'test/test_src/' + path.replace('/', '_') + '.pas'

        from Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        interpreter = Interpreter(program)
        interpreter.interpret()

        scopes_true = [
            ['builtins', 0, None],
            ['global', 1, 'builtins'],
            ['ALPHA', 2, 'global'],
            ['ALPHA2', 2, 'global'],
            ['BETA', 3, 'ALPHA'],
        ]

        self.assertEqual(
            scopes_true,
            [
                [
                    node.scope.scope_name,
                    node.scope.scope_level,
                    node.scope.enclosing_scope.scope_name if node.scope.enclosing_scope else None,
                ]
                for node in interpreter.ar_tree.bf_traverse(interpreter.ar_tree.root)
            ],
        )


if __name__ == '__main__':
    unittest.main()
