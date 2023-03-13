# Limbo

A parser combinator library for Python.


```py
"""
A parser for propositional logic.
"""

from limbo imort Match, All, Any, Use


Literal = Match("[A-Z]")


UnaryExpression = All(
    Match("¬"),
    Use('Expression'),  # RHS
)


BinaryExpression = All(
    Match("("),
    Use('Expression')   # LHS
    Any(
      Match("v"),       # Disjunction
      Match("^"),       # Conjunction
      Match(">"),       # Implication
    ),
    Use('Expression'),  # RHS
    Match(")"),
)


Expression = Any(
    Literal,
    UnaryExpression,    # No need for `Use()` since the 
    BinaryExpression,   # terms are already defined.
)
```
