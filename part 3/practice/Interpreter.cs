using System;

public class Interpreter
{
	int Position { get; set; }
	string Text { get; init; }
	int Len { get { return this.Text.Length; } }

	List<Token> Tokens { get; set; }

	public Interpreter(string text)
	{
        Text = text;
		Tokens = new List<Token>();
	}

	private void Skip()
	{
		while (Char.IsWhiteSpace(Text[Position+1])) { Position++; }
	}

	private void Next()
	{
		if (Position < Len)
		{
			Position++;
		}
	}

	private Token TokenizeInt()
	{
		string number = Text[Position].ToString();

		while (Position < Len - 1 && Char.IsDigit(Text[Position+1]))
		{
			number += Text[++Position];
		}

		//Position++;

		return new Token(Token.INT, number);
	}

	private void Error()
	{
		throw new Exception($"Invalid element exception. {Text[Position]} was not expected.");
	}

	public void Tokenize()
	{
		while (Position < Len)
		{
			switch (Text[Position])
			{
				case ' ':
					Skip();
					break;

				case '+':
                    Tokens.Add(new Token(Token.PLUS, "+"));
					break;

				case '-':
                    Tokens.Add(new Token(Token.MINUS, "-"));
					break;

				default:
					if (Char.IsDigit(Text[Position]))
					{
						Tokens.Add(TokenizeInt());
					} else
					{
						Error();
					}
					break;

			}

            Next();
        }
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
				Error();
				return -1;
		}
	}

	public int Eval()
	{
		Tokenize();

		int result = int.Parse(Tokens[0].Value);

		for (int i = 1; i < Tokens.Count(); )
		{
			result = Op(result, Tokens[i++].Value, int.Parse(Tokens[i++].Value));
		}

		return result;
	}
}
