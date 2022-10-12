using System;


    public class Token
    {
        public static string PLUS = "PLUS";
        public static string MINUS = "MINUS";
        public static string INT = "INT";

        public string Type { get; set; }
        public string Value { get; set; }

        public Token(string type, string value) {
            this.Type = type;
            this.Value = value;
        }

        public override string ToString()
        {
            return $"Type: {Type}, Value: {Value}";
        }
    }
