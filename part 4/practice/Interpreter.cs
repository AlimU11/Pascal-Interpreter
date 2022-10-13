using System;
using test.@base;

namespace test.part_4.practice
{
    public class Interpreter : IInterpreter
    {
        Lexer lexer { get; init; }

        public Interpreter(string text)
        {
            lexer = new Lexer(text);
        }

        private static void Error(string text)
        {
            throw new Exception($"Invalid element exception. {text} was not expected.");
        }

        private int Op(int left, string op, int right)
        {
            switch (Char.Parse(op))
            {
                case '+':
                    return left + right;

                case '-':
                    return left - right;

                default:
                    Error(op);
                    return -1;
            }
        }

        private int Term(int idx)
        {
            return int.Parse(lexer.Tokens[idx].Value);
        }

        private static int Eval(int left, string op, int right)
        {
            switch(op)
            {
                case "+":
                    return left + right;

                case "-":
                    return left - right;

                case "*":
                    return left * right;

                case "/":
                    return left / right;

                default:
                    Error(op);
                    return -1;
            }
        }

        public int Eval()
        {
            lexer.Tokenize();

            int result = Term(0);

            for (int i = 1; i < lexer.Tokens.Count();)
            {
                string op = lexer.Tokens[i++].Value;
                int right = Term(i++);
                result = Eval(result, op, right);
            }

            return result;
        }
    }
}
