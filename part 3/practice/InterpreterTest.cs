using NUnit.Framework;
using System.Text.RegularExpressions;

namespace practice
{
    [TestFixture]
    public class InterpreterTests
    {
        [Test, TestCaseSource(nameof(DataProvider))]
        public void TestMethod1(string test, int expected)
        {
            Assert.That((new Interpreter(test)).Eval() == expected);
        }

        public static IEnumerable<TestCaseData> DataProvider()
        {
            var arr = File.ReadAllLines("../../../part 3_lesson.txt").ToList()
                .Select(x =>
                Regex.Match(x, @"\('(.+)'.*,.?(\d+)\)").Groups.Values.ToArray())
                .Select(x => new string[] { x[1].ToString(), x[2].ToString() }).ToList();

            foreach (var pair in arr)
            {
                yield return new TestCaseData(pair[0], int.Parse(pair[1]));
            }
        }
    }
}
