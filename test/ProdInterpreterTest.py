import ast
import os
import unittest

from TestMethods import TestMethods


class ProdInterpreterTestCase(TestMethods):
    def test_base(self):
        src_test = [
            ProdInterpreterTestCase.base + 'test/test_src/' + i
            for i in os.listdir(ProdInterpreterTestCase.base + 'test/test_src/')
            if 'base' in i and i.endswith('.txt')
        ]

        src_program = [
            ProdInterpreterTestCase.base + 'test/test_src/' + i
            for i in os.listdir(ProdInterpreterTestCase.base + 'test/test_src/')
            if 'base' in i and i.endswith('.pas')
        ]

        self.import_modules('base')

        from Interpreter import Interpreter

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

        self.delete('base')


if __name__ == '__main__':
    unittest.main()
