# Part 7 - Practice

## Grammar

```ebnf
<expression> ::= <term> { ("+" | "-") <term> }*
<term>       ::= <factor> { ("*" | "/") <factor> }*
<factor>     ::= <INTEGER> | "(" <expression> ")"
<INTEGER>    ::= <digit>+
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

1. Write a translator (hint: node visitor) that takes as input an arithmetic expression and prints it out in postfix notation, also known as Reverse Polish Notation (RPN). For example, if the input to the translator is the expression (5 + 3) * 12 / 3 than the output should be 5 3 + 12 * 3 /. See the answer here but try to solve it first on your own.

2. Write a translator (node visitor) that takes as input an arithmetic expression and prints it out in LISP style notation, that is 2 + 3 would become (+ 2 3) and (2 + 3 * 5) would become (+ 2 (* 3 5)). You can find the answer here but again try to solve it first before looking at the provided solution.

## Reference

https://ruslanspivak.com/lsbasi-part7/
