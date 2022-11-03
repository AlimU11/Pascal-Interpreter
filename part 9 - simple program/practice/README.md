# Part 9 - Practice

## Grammar

```ebnf
<program> ::= <compound_statement> <DOT>

<compound_statement> ::= <BEGIN> <statement_list> <END>

<statement_list> ::= <statement> { <SEMI> <statement_list> }*

<statement> ::= <compound_statement>
              | <assignment_statement>
              | <empty>

<assignment_statement> ::= <variable> <ASSIGN> <expression>

<empty> ::= ''

<factor> ::= <PLUS> <factor>
           | <MINUS> <factor>
           | <INTEGER>
           | <LPAREN> <expression> <RPAREN>
           | <variable>

<expression> ::= <term> { (<PLUS> | <MINUS>) <term> }*

<term> ::= <factor> { (<MUL> | <DIV>) <factor> }*

<variable> ::= <ID>

<ID> ::= [a-zA-Z_][a-zA-Z0-9_]*

<INTEGER> ::= <digit>+

<digit> ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

<BEGIN> ::= 'BEGIN'
<END> ::= 'END'
<DOT> ::= '.'
<SEMI> ::= ';'
<ASSIGN> ::= ':='
<PLUS> ::= '+'
<MINUS> ::= '-'
<MUL> ::= '*'
<DIV> ::= 'DIV'
<LPAREN> ::= '('
<RPAREN> ::= ')'

```

## Diagram

### Program

![](src/diagram1.svg)

### Compound Statement

![](src/diagram2.svg)

### Statement List

![](src/diagram3.svg)

### Statement

![](src/diagram4.svg)

### Assignment Statement

![](src/diagram5.svg)

### Variable

![](src/diagram6.svg)

### Empty Statement

![](src/diagram7.svg)

### Factor

![](src/diagram8.svg)

### Expression

![](src/diagram9.svg)

### Term

![](src/diagram10.svg)

## Tasks

1. Pascal variables and reserved keywords are case insensitive, unlike in many other programming languages, so BEGIN, begin, and BeGin they all refer to the same reserved keyword. Update the interpreter so that variables and reserved keywords are case insensitive. Use the following program to test it:

```pascal
BEGIN

    BEGIN
        number := 2;
        a := NumBer;
        B := 10 * a + 10 * NUMBER / 4;
        c := a - - b
    end;

    x := 11;
END.
```

2. I mentioned in the “hacks” section before that our interpreter is using the forward slash character ‘/’ to denote integer division, but instead it should be using Pascal’s reserved keyword div for integer division. Update the interpreter to use the div keyword for integer division, thus eliminating one of the hacks.

3. Update the interpreter so that variables could also start with an underscore as in ‘_num := 5’.

## Reference

https://ruslanspivak.com/lsbasi-part9/
