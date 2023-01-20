import ast
import os
import sys
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

        sys.path.append(ProdInterpreterTestCase.base + 'base')

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
        sys.path.remove(ProdInterpreterTestCase.base + 'base')


if __name__ == '__main__':
    unittest.main()
