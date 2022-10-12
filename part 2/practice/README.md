# Part 2 - Practice

## Grammar

```ebnf
<expression> ::= <term> { <op> <term> }+
<term>       ::= <whitespace>* <factor> <whitespace>*
<factor>     ::= <number>
<number>     ::= <digit>+
<op>         ::= "+" | "-"  | "*" | "/" ;
<whitespace> ::= " "
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

## Tasks

1. Extend the calculator to handle multiplication of two integers
2. Extend the calculator to handle division of two integers
3. Modify the code to interpret expressions containing an arbitrary number of additions and subtractions, for example “9 - 5 + 3 + 11”

## Reference

https://ruslanspivak.com/lsbasi-part2/
