# Part 3 - Practice

## Grammar

```ebnf
<expression> ::= <term> { <op> <term> }*
<term>       ::= <whitespace>* <factor> <whitespace>*
<factor>     ::= <number>
<number>     ::= <digit>+
<op>         ::= "*" | "/"
<whitespace> ::= " "
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

## Diagram

![](diagram.svg)

## Tasks

1. Draw a syntax diagram for arithmetic expressions that contain only multiplication and division, for example “7 * 4 / 2 * 3”. Seriously, just grab a pen or a pencil and try to draw one.

2. Modify the source code of the calculator to interpret arithmetic expressions that contain only multiplication and division, for example “7 * 4 / 2 * 3”.

3. Write an interpreter that handles arithmetic expressions like “7 - 3 + 2 - 1” from scratch. Use any programming language you’re comfortable with and write it off the top of your head without looking at the examples. When you do that, think about components involved: a lexer that takes an input and converts it into a stream of tokens, a parser that feeds off the stream of the tokens provided by the lexer and tries to recognize a structure in that stream, and an interpreter that generates results after the parser has successfully parsed (recognized) a valid arithmetic expression. String those pieces together. Spend some time translating the knowledge you’ve acquired into a working interpreter for arithmetic expressions.


## Reference

https://ruslanspivak.com/lsbasi-part3/
