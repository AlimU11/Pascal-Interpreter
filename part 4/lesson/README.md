# Part 4 - Lesson

## Grammar

```ebnf
<expression> ::= <term> { <op> <term> }*
<term>       ::= <whitespace>* <factor> <whitespace>*
<factor>     ::= <number>
<number>     ::= <digit>+
<op>         ::= "*" | "/" ;
<whitespace> ::= " "
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

## Diagram

![](diagram.svg)

## Reference

https://ruslanspivak.com/lsbasi-part4/
