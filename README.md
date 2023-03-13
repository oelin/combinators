# Limbo

A parser combinator library for Python.


## Examples

An example of a parser for propositional logic using Limbo.

```py
>>> from limbo import Match, All, Any, Use

>>> Literal = Match("[A-Z]")

>>> UnaryExpression = All()(
        Match("¬"),
        (lambda p: Expression(p)), # RHS
    )

>>> BinaryExpression = All()(
        Match("\("),
        (lambda p: Expression(p)), # LHS
        Any()(
            Match("v"),            # Disjunction
            Match("\^"),           # Conjunction
            Match(">"),            # Implication
        ),
        (lambda p: Expression(p)), # RHS
        Match("\)"),
    )

>>> Expression = Any()(
        Literal,
        UnaryExpression,            
        BinaryExpression,
    )
```

The parser can be called as a function. For example:

```py
>>> from limbo import Parse

>>> input = Parse('(A>¬B)') # A implies not B.

>>> Expression(input)

Parse(
    string='', 
    result=('(', 'A', '>', ('¬', 'B'), ')'), 
    failed=False
)
```
