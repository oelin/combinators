"""
Implements common concrete parsers.
"""

from . combinators import *
from dataclasses import dataclass
from re import match


@dataclass
class Match(Parser):
    """
    Implements the match parser. This parser consumes a single lexeme
    from the parse string.

    Parameters
    ----------

    pattern: str

        A regular expression describing the set of lexemes to match.

    Example
    -------

    >>> number = Match("\d")
    >>> letter = Match("[a-z]")
    >>> letter(("hello world", None))

    ("ello world", "h")

    >>> number(("hello world", None))

    None

    >>> number(("1234", None))

    ("234", "1")
    """

    pattern: str


    def __call__(self, parse: Parse) -> Parse:

        string = parse[0]
        lexeme = match(self.pattern, string)

        if lexeme:
            return string[lexeme.end() :], lexeme.group()


    def __repr__(self) -> str:
        return f'"{self.pattern}"'
