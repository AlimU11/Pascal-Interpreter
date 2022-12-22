import ast
import os
import pathlib
import sys
import unittest


class InterpreterTestCase(unittest.TestCase):
    base = pathlib.Path(__file__).parent.parent.resolve().__str__() + '/'

    def import_modules(self, path):
        test = InterpreterTestCase.base + path
        src_test = InterpreterTestCase.base + '/test/test_src/' + path.replace('/', '_') + '.txt'
        sys.path.append(test)
        sys.path.append(src_test)

        return src_test

    def delete(self, path):
        del sys.modules['Interpreter']
        del sys.modules['Token']

        if 'Lexer' in sys.modules:
            del sys.modules['Lexer']

        if 'Parser' in sys.modules:
            del sys.modules['Parser']

        if 'Node' in sys.modules:
            del sys.modules['Node']

        if 'AST' in sys.modules:
            del sys.modules['AST']

        if 'SymbolTable' in sys.modules:
            del sys.modules['SymbolTable']

        if 'Symbol' in sys.modules:
            del sys.modules['Symbol']

        sys.path.remove(InterpreterTestCase.base + path)

    def abstract_calc_test(self, path):
        src_test = self.import_modules(path)

        from Interpreter import Interpreter

        with open(src_test, 'r') as f:
            test_pairs = [ast.literal_eval(i) for i in f.readlines()]

        for test, expected in test_pairs:
            with self.subTest(test=test, expected=expected):
                self.assertEqual(Interpreter(test).expr(), expected)

        self.delete(path)

    def abstract_program_test(self, path):
        src_test = self.import_modules(path)
        src_program = InterpreterTestCase.base + 'test/test_src/' + path.replace('/', '_') + '.pas'

        from Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        with open(src_test, 'r') as f:
            global_scope = ast.literal_eval(f.read())

        interpreter = Interpreter(program)
        interpreter.interpret()

        self.assertEqual(interpreter.GLOBAL_SCOPE, global_scope)
        self.delete(path)

    def test_part1_lesson(self):
        self.abstract_calc_test('part 1 - simple arithmetic interpreter/lesson')

    def test_part1_practice(self):
        self.abstract_calc_test('part 1 - simple arithmetic interpreter/practice')

    def test_part2_lesson(self):
        self.abstract_calc_test('part 2/lesson')

    def test_part2_practice(self):
        self.abstract_calc_test('part 2/practice')

    def test_part3_lesson(self):
        self.abstract_calc_test('part 3/lesson')

    def test_part3_practice(self):
        self.abstract_calc_test('part 3/practice')

    def test_part4_lesson(self):
        self.abstract_calc_test('part 4/lesson')

    def test_part4_practice(self):
        self.abstract_calc_test('part 4/practice')

    def test_part5_lesson(self):
        self.abstract_calc_test('part 5 - operators precedence/lesson')

    def test_part5_practice(self):
        self.abstract_calc_test('part 5 - operators precedence/practice')

    def test_part6_lesson(self):
        self.abstract_calc_test('part 6/lesson')

    def test_part7_lesson(self):
        self.abstract_calc_test('part 7 - AST/lesson')

    def test_part7_practice(self):
        self.abstract_calc_test('part 7 - AST/practice')

    def test_part8_lesson(self):
        self.abstract_calc_test('part 8 - unary operators/lesson')

    def test_part9_lesson(self):
        self.abstract_program_test('part 9 - simple program/lesson')

    def test_part9_practice(self):
        self.abstract_program_test('part 9 - simple program/practice')

    def test_part10_lesson(self):
        self.abstract_program_test('part 10 - complete program/lesson')

    def test_part11_lesson(self):
        self.abstract_program_test('part 11 - symbol tables/lesson')

    def test_base(self):

        src_test = [
            InterpreterTestCase.base + 'test/test_src/' + i
            for i in os.listdir(InterpreterTestCase.base + 'test/test_src/')
            if 'base' in i and i.endswith('.txt')
        ]

        src_program = [
            InterpreterTestCase.base + 'test/test_src/' + i
            for i in os.listdir(InterpreterTestCase.base + 'test/test_src/')
            if 'base' in i and i.endswith('.pas')
        ]

        sys.path.append(InterpreterTestCase.base + 'base')

        from base.Interpreter import Interpreter

        for test, program in zip(src_test, src_program):

            test_filename = test.split('/')[-1].split('.')[0]
            program_filename = program.split('/')[-1].split('.')[0]

            with open(test, 'r') as f:
                global_scope = ast.literal_eval(f.read())

            with open(program, 'r') as f:
                program_text = f.read()

            with self.subTest(test=program_filename, expected=test_filename):
                interpreter = Interpreter(program_text)
                interpreter.interpret()
                self.assertEqual(interpreter.GLOBAL_SCOPE, global_scope)

        del sys.modules['base.Interpreter']
        del sys.modules['base.Symbol']
        del sys.modules['base.SymbolTable']
        del sys.modules['base.Token']
        del sys.modules['base.Lexer']
        del sys.modules['base.Parser']
        del sys.modules['base.NodeVisitor']
        del sys.modules['base.AST']
        del sys.modules['base']
        sys.path.remove(InterpreterTestCase.base + 'base')


if __name__ == '__main__':
    unittest.main()
