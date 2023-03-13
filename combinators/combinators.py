"""
Implements parser combinators for fundemental grammar constructs such
as concatenation and alternation.
"""


from typing import Any, Tuple, Optional
from dataclasses import dataclass


Parse = Optional[Tuple[str, Any]]


class Parser:

    def __call__(self, parse: Parse) -> Parse:
        raise NotImplementedError()


class Nothing(Parser):
    """
    Implements the nothing parser, also known as epsilon. This parser
    does nothing.
    """

    __call__ = lambda _, parse: parse
    __repr__ = lambda _: 'ɛ'


# Parser combinators.

def And(p: Parser, q: Parser) -> Parser:
    """
    Implements the concatenation/conjunction parser combinator. This
    parser combinator takes in two parsers and returns a new parser
    which calls them in series.

    Parameters
    ----------

    p: Parser

        The first parser.

    q: Parser

        The second parser.

    Returns
    -------

    parser: Parser

        The concatenation of p and q.

    Example
    -------

    >>> number = Match("\d")
    >>> letter = Match("[a-z]")
    >>> number & letter

    "\d" "[a-z]"
    """

    class AndParser(Parser):

        __call__ = lambda _, parse: (parse := p(parse)) and q(parse)
        __repr__ = lambda _: f'{p} {q}'

    return AndParser()


def Or(p: Parser, q: Parser) -> Parser:
    """
    Implements the alternation/disjunction parser combinator. This
    parser combinator takes in two parsers and returns a new parser
    that calls them in paralell.

    Parameters
    ----------

    p: Parser

        The first parser.

    q: Parser

        The second parser.

    Returns
    -------

    parser: Parser

        The alternation of p and q.

    Example
    -------

    >>> number = Match("\d")
    >>> letter = Match("\[a-z]")
    >>> number | letter

    ("\d" | "[a-z]")
    """

    class OrParser(Parser):

        __call__ = lambda _, parse: p(parse) or q(parse)
        __repr__ = lambda _: f'({p} | {q})'

    return OrParser()


def Maybe(p: Parser) -> Parser:
    """
    Implements the maybe/optional parser combinator. This parser
    combinator takes in a parser and returns a new parser which
    optionally calls it.

    Parameters
    ----------

    p: Parser

        The parser.

    Returns
    -------

    parser: Parser

        The optional of p.

    Example
    -------

    >>> number = Match("\d")
    >>> Maybe(number)

    ["\d"]
    """

    class MaybeParser(Parser):

        __call__ = lambda _, parse: p(parse) or parse
        __repr__ = lambda _: f'[{p}]'

    return MaybeParser()


def Lambda(p: Parser) -> Parser:
    """
    Implements the lambda parser combinator. This parser combinator
    takes a parser and returns an identical parser constructed
    with `Parser`.

    Parameters
    ----------

    p: Parser

        The parser.

    Returns
    -------

    parser: Parser

        An identical parser to `p` constructed with `Parser`.

    Example
    -------

    >>> # Lazy evaluation using `Lambda`.
    >>> number = Match("\d")
    >>> numbers = number & Lambda(lambda p: numbers(p)) | number
    >>> numbers("123")

    ('', ('1', ('2', '3')))
    """

    class LambdaParser(Parser):
        __call__ = lambda _, parse: p(parse)
        __repr__ = lambda _: 'λ'

    return LambdaParser()
