# Limbo

A parser combinator library for Python.


```py
# Parser for propositional logic.

from limbo imort Match, All, Any

Literal = Match("[A-Z]")

UnaryExpression = All(
  Match("¬"),
  lambda: Expression(), # RHS
)

BinaryExpression = All(
  Match("("),
  lambda: Expression(), # LHS
  Any(
    Match("v"), # Disjunction
    Match("^"), # Conjunction
    Match(">"), # Implication
  ),
  lambda: Expression(), # RHS
  Match(")"),
)

Expression = Any(
  Literal,
  UnaryExpression,
  BinaryExpression,
)
```
