import ast
import pathlib
import sys
import unittest


class TestMethods(unittest.TestCase):
    base = pathlib.Path(__file__).parent.parent.resolve().__str__() + '/'

    def import_modules(self, path):
        test = TestMethods.base + path
        src_test = TestMethods.base + '/test/test_src/' + path.replace('/', '_') + '.txt'
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

        sys.path.remove(TestMethods.base + path)

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
        src_program = TestMethods.base + 'test/test_src/' + path.replace('/', '_') + '.pas'

        from Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        with open(src_test, 'r') as f:
            global_scope = ast.literal_eval(f.read())

        interpreter = Interpreter(program)
        interpreter.interpret()

        self.assertEqual(interpreter.GLOBAL_SCOPE, global_scope)
        self.delete(path)

    def abstract_test_pass(self, path):
        src_program = TestMethods.base + 'test/test_src/' + path + '.pas'

        from Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        interpreter = Interpreter(program)
        interpreter.interpret()

    def abstract_test_fail(self, path, exception=Exception):
        src_program = TestMethods.base + 'test/test_src/' + path

        from Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        interpreter = Interpreter(program)

        with self.assertRaises(exception):
            interpreter.interpret()
