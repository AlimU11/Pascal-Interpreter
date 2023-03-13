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
        # if 'Interpreter' in sys.modules:
        #     del sys.modules['Interpreter']

        # self.import_modules("part 14 - nested scopes/practice")

        # from Interpreter import Interpreter

        # with open(
        #     TestMethods.base
        #     + "/test/test_src/"
        #     + "part 14 - nested scopes_practice.pas",
        #     "r",
        # ) as f:
        #     program = f.read()

        # interpreter = Interpreter(program)
        # interpreter.interpret()

        # scopes_true = [
        #     ["builtins", 0, None],
        #     ["global", 1, "builtins"],
        #     ["ALPHAA", 2, "global"],
        #     ["BETA", 3, "ALPHAA"],
        #     ["GAMMA", 4, "BETA"],
        #     ["ALPHAB", 2, "global"],
        # ]

        # scopes = []

        # for scope in interpreter.semantic_analyzer.scopes:
        #     scopes.append(
        #         [
        #             scope.scope_name,
        #             scope.scope_level,
        #             scope.enclosing_scope.scope_name if scope.enclosing_scope else None,
        #         ]
        #     )

        # self.assertEqual(scopes, scopes_true)


if __name__ == '__main__':
    unittest.main()
