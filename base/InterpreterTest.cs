using NUnit.Framework;
using System.Text.RegularExpressions;

namespace test.@base
{
    [TestFixture]
    public class InterpreterTests
    {
        [Test, TestCaseSource(nameof(DataProvider))]
        public void TestMethod1(string i_namespace, string text, int expected)
        {
            IInterpreter? i = TestData.GetInterpreter(text, i_namespace);
            Assert.IsNotNull(i);
            Assert.That(i.Eval(), Is.EqualTo(expected));
        }

        public static IEnumerable<TestCaseData> DataProvider()
        {
            foreach (var file in TestData.TestFiles)
            {
                var arr = File.ReadAllLines(file).ToList().Select(x =>
                Regex.Match(x, @"\('(.+)'.*,.?([-]?\d+)\)").Groups.Values.ToArray())
                .Select(x => new string[] { x[1].ToString(), x[2].ToString() }).ToList();

                foreach (var pair in arr)
                {
                    yield return new TestCaseData(Regex.Match(file, @"\d+.*_(lesson|practice)").ToString(), pair[0], int.Parse(pair[1]));
                }
            }
        }
    }
}
