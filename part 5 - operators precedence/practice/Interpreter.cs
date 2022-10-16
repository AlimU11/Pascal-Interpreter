using System;
using test.@base;

namespace test.part_5.practice
{
    public class Interpreter : IInterpreter
    {
        Lexer lexer { get; init; }

        public Interpreter(string text)
        {
            lexer = new Lexer(text);
            lexer.Tokenize();
            lexer.Position = 0;
        }

        private static void Error(string text)
        {
            throw new Exception($"Invalid element exception. {text} was not expected.");
        }

        private int Factor()
        {
            if (lexer.Tokens[lexer.Position].Type == Token.INT)
            {
                return int.Parse(lexer.Tokens[lexer.Position++].Value);
            } else if (lexer.Tokens[lexer.Position++].Type == Token.LPAREN)
            {
                int result = Eval();
                lexer.Position++;
                return result;
            } else
            {
                Error(lexer.Tokens[lexer.Position].Value);
                return -1;
            }
        }

        private int Term()
        {
            int result = Factor();

            while (lexer.Position < lexer.Tokens.Count()
                && (lexer.Tokens[lexer.Position].Type == Token.MULTIPLY || lexer.Tokens[lexer.Position].Type == Token.DIVIDE))
            {
                string op = lexer.Tokens[lexer.Position++].Value;
                int right = Factor();

                result = Eval(result, op, right);
            }

            return result;
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
            int result = Term();

            while (lexer.Position < lexer.Tokens.Count() &&
                (lexer.Tokens[lexer.Position].Type == Token.PLUS || lexer.Tokens[lexer.Position].Type == Token.MINUS))
            {
                string op = lexer.Tokens[lexer.Position++].Value;
                int right = Term();
                result = Eval(result, op, right);
            }

            return result;
        }
    }
}
