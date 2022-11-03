using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using test.@base;

namespace test.@base
{
    public class TestData
    {
        static string BASE = "../../../test/test_src/";

        public static List<string> TestFiles = (new List<string>() {
            "part 3_lesson.txt",
            "part 4_practice.txt",
            "part 5 - operators precedence_practice.txt"
        }).Select(x => BASE + x).ToList();

        public static IInterpreter? GetInterpreter(string text, string i_namespace)
        {
            Console.WriteLine(i_namespace);
            switch (i_namespace)
            {
                case "3_lesson":
                    return new test.part_3.practice.Interpreter(text);

                case "4_practice":
                    return new test.part_4.practice.Interpreter(text);

                case "5 - operators precedence_practice":
                    return new test.part_5.practice.Interpreter(text);
            }

            return null;
        }
    }
}
