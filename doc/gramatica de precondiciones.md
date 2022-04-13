# Especificación de la gramática de las precondiciones

```bnf
<inicio>      ::= <atomo> | <atomo> <condicion>

<condicion>   ::= <operacion> <atomo> <condicion> | <empty>

<atomo>       ::= variable ' is ' valor | 'not ' varialbe ' is ' valor

<operacion>   ::= 'and' | 'or'

```
