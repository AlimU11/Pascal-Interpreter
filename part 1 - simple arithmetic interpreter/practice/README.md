# Part 1 - Practice

## Grammar

```ebnf
<expression> ::= <term> <op> <term>
<term>       ::= <whitespace>* <factor> <whitespace>*
<factor>     ::= <number>
<number>     ::= <digit>+
<op>         ::= "+" | "-"
<whitespace> ::= " "
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```


## Tasks

1. Modify the code to allow multiple-digit integers in the input, for example “12+3”
2. Add a method that skips whitespace characters so that your calculator can handle inputs with whitespace characters like ” 12 + 3”
3. Modify the code and instead of ‘+’ handle ‘-‘ to evaluate subtractions like “7-5”

## Reference

https://ruslanspivak.com/lsbasi-part1/
