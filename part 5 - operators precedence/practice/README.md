# Part 5 - Practice

## Grammar

```ebnf
<expression> ::= <term> { ("+" | "-") <term> }*
<term>       ::= <factor> { ("*" | "/") <factor> }*
<factor>     ::= <number> | "(" <expression> ")"
<number>     ::= <digit>+
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

## Diagram

### Expr
![](diagram1.svg)

### Term
![](diagram2.svg)

### Factor
![](diagram3.svg)

## Tasks
1. Write an interpreter as described in this article off the top of your head, without peeking into the code from the article. Write some tests for your interpreter, and make sure they pass.

2. Extend the interpreter to handle arithmetic expressions containing parentheses so that your interpreter could evaluate deeply nested arithmetic expressions like: 7 + 3 * (10 / (12 / (3 + 1) - 1))

## Reference

https://ruslanspivak.com/lsbasi-part5/
