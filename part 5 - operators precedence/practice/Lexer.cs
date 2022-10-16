using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace test.part_5.practice
{
    public class Lexer
    {
        public int Position { get; set; }
        string Text { get; init; }
        int Len { get { return this.Text.Length; } }

        public List<Token> Tokens { get; private set; }

        public Lexer(string text)
        {
            Text = text;
            Tokens = new List<Token>();
        }

        private void Error()
        {
            throw new Exception($"Invalid element exception. {Text[Position]} was not expected.");
        }

        private void Skip()
        {
            while (HasNext() && Char.IsWhiteSpace(Text[Position])) { }
        }

        private bool HasNext()
        {
            return ++Position < Len;
        }

        private Token TokenizeInt()
        {
            string number = Text[Position].ToString();

            while (Position < Len - 1 && Char.IsDigit(Text[Position + 1]))
            {
                number += Text[++Position];
            }

            return new Token(Token.INT, number);
        }

        public void Tokenize()
        {
            while (Position < Len)
            {
                switch (Text[Position])
                {
                    case ' ':
                        Skip();
                        continue;

                    case '+':
                        Tokens.Add(new Token(Token.PLUS, "+"));
                        break;

                    case '-':
                        Tokens.Add(new Token(Token.MINUS, "-"));
                        break;

                    case '*':
                        Tokens.Add(new Token(Token.MULTIPLY, "*"));
                        break;

                    case '/':
                        Tokens.Add(new Token(Token.DIVIDE, "/"));
                        break;

                    case '(':
                        Tokens.Add(new Token(Token.LPAREN, "("));
                        break;

                    case ')':
                        Tokens.Add(new Token(Token.RPAREN, ")"));
                        break;

                    default:
                        if (Char.IsDigit(Text[Position]))
                        {
                            Tokens.Add(TokenizeInt());
                        }
                        else
                        {
                            Error();
                        }
                        break;

                }
                HasNext();
            }
        }
    }
}
