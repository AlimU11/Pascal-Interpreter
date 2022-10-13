# Part 4 - Practice

## Grammar

```ebnf
<expression> ::= <term> { <op> <term> }*
<term>       ::= <whitespace>* <factor> <whitespace>*
<factor>     ::= <number>
<number>     ::= <digit>+
<op>         ::= "+" | "-" | "*" | "/"
<whitespace> ::= " "
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

## Diagram

![](diagram.svg)

## Tasks
1. Write a grammar that describes arithmetic expressions containing any number of +, -, *, or / operators. With the grammar you should be able to derive expressions like “2 + 7 * 4”, “7 - 8 / 4”, “14 + 2 * 3 - 6 / 2”, and so on.

2. Using the grammar, write an interpreter that can evaluate arithmetic expressions containing any number of +, -, *, or / operators. Your interpreter should be able to handle expressions like “2 + 7 * 4”, “7 - 8 / 4”, “14 + 2 * 3 - 6 / 2”, and so on

## Reference

https://ruslanspivak.com/lsbasi-part4/
