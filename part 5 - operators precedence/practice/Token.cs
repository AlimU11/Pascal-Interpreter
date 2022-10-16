using System;

namespace test.part_5.practice
{
    public class Token
    {
        public static string PLUS = "PLUS";
        public static string MINUS = "MINUS";
        public static string MULTIPLY = "MULTIPLY";
        public static string DIVIDE = "DIVIDE";
        public static string INT = "INT";
        public static string LPAREN = "LPAREN";
        public static string RPAREN = "RPAREN";

        public string Type { get; set; }
        public string Value { get; set; }

        public Token(string type, string value)
        {
            this.Type = type;
            this.Value = value;
        }

        public override string ToString()
        {
            return $"Type: {Type}, Value: {Value}";
        }
    }
}
