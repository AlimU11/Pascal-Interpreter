# Part 17 - Practice

## Grammar

```ebnf
# Program

<program> ::= <PROGRAM> <variable> <SEMI> <block> <DOT>

# Block

<block> ::= <declarations> <compound_statement>

# Declaration

<declarations> ::= <VAR> { <variable_declaration> <SEMI> }+
                | { <PROCEDURE> <ID> <SEMI> <block> <SEMI> }*
                | <empty>

<variable_declaration> ::= <ID> { <COMMA> <ID> }* <COLON> <type_spec>

<type_spec> ::= <INTEGER_TYPE> | <REAL_TYPE>

# Statement

<compound_statement> ::= <BEGIN> <statement_list> <END>

<statement_list> ::= <statement> { <SEMI> <statement_list> }*

<statement> ::= <compound_statement>
              | <procedure_call_statement>
              | <assignment_statement>
              | <empty>

<assignment_statement> ::= <variable> <ASSIGN> <expression>

<procedure_call_statement> ::= <ID> <LPAREN> [ <expression> { <COMMA> <expression> }* ] <RPAREN>

<empty> ::= ''

# Mathemathical Expression

<expression> ::= <term> { (<PLUS> | <MINUS>) <term> }*

<term> ::= <factor> { (<MUL> | <INTEGER_DIV> | <FLOAT_DIV>) <factor> }*

<factor> ::= <PLUS> <factor>
           | <MINUS> <factor>
           | <INTEGER>
           | <REAL>
           | <LPAREN> <expression> <RPAREN>
           | <variable>

# Variables

<variable> ::= <ID>

<ID> ::= [a-zA-Z_][a-zA-Z0-9_]*

# Numerical Values

<INTEGER> ::= <digit>+
<REAL> ::= <digit>+ [ <DOT> <digit>+ ]

<digit> ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

# Reserved words

<PROGRAM> ::= 'PROGRAM'
<BEGIN> ::= 'BEGIN'
<END> ::= 'END'
<VAR> ::= 'VAR'
<INTEGER_TYPE> ::= 'INTEGER'
<REAL_TYPE> ::= 'REAL'

# Symbols

<DOT> ::= '.'
<SEMI> ::= ';'
<COMMA> ::= ','
<COLON> ::= ':'
<LPAREN> ::= '('
<RPAREN> ::= ')'

# Operators

<ASSIGN> ::= ':='
<PLUS> ::= '+'
<MINUS> ::= '-'
<MUL> ::= '*'
<FLOAT_DIV> ::= '/'
<INTEGER_DIV> ::= 'DIV'
```

## Diagram

### Program

![](src/diagram1.svg)

### Block

![](src/diagram2.svg)

### Declarations

![](src/diagram3.svg)

### Variable Declaration

![](src/diagram4.svg)

### Type Specification

![](src/diagram5.svg)

### Compound Statement

![](src/diagram6.svg)

### Statement List

![](src/diagram7.svg)

### Statement

![](src/diagram8.svg)

### Assignment Statement

![](src/diagram9.svg)

### Procedure Call Statement

![](src/diagram10.svg)

### Empty Statement

![](src/diagram11.svg)

### Expression

![](src/diagram12.svg)

### Term

![](src/diagram13.svg)

### Factor

![](src/diagram14.svg)

### Variable

![](src/diagram15.svg)

## Tasks

Add a check to the semantic analyzer that verifies that the number of arguments (actual parameters) passed to a procedure call equals the number of formal parameters defined in the corresponding procedure declaration. Let’s take the Alpha procedure declaration we used earlier in the article as an example:

```pascal
program Main;

procedure Alpha(a : integer; b : integer);
var x : integer;
begin
   x := (a + b ) * 2;
end;

begin { Main }

   Alpha(3 + 5, 7);  { procedure call }

end.  { Main }
```

## Reference

https://ruslanspivak.com/lsbasi-part17/
