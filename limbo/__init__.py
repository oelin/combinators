from typing import Any, Callable, Tuple
from dataclasses import dataclass


# Types for parses, parsers and parser combinators.

@dataclass
class Parse:
    """
    Parse

    An abstract base class for parses.
    """

    string: str
    result: Any
    failed: bool = False


class Parser:
    """
    Parser

    An abstract base class for parsers (transformations on parses).
    """

    def __call__(self, parse: Parse) -> Parse:
        raise NotImplementedError()


class ParserCombinator:
    """
    ParserCombinator

    An abstract base class for parser combinators (transformations
    on parsers).
    """

    def __call__(self, *parsers: Tuple[Parser]) -> Parser:
        raise NotImplementedError()


# Parsers.

class Success(Parser):
    """
    Success(Parser)

    Makes any Parse a success.
    """

    def __call__(parse: Parse) -> Parse:
        return Parse(
                string = parse.string,
                result = parse.result,
                failed = False,
        )


class Failure(Parser):
    """
    Failure(Parser)

    Makes any Parse a failure.
    """

    def __call__(parse: Parse) -> Parse:
        return Parse(
                string = parse.string,
                result = parse.result,
                failed = True,
        )


class Nothing(Parser):
    """
    Nothing(Parser)

    Parsers the the empty string (i.e. epsilon). Reduces to the
    identity function so that `Nothing(parse) = parse`.
    """

    def __call__(parse: Parse) -> Parse:
        return Parse(
                string = parse.string,
                result = parse.result,
                failed = parse.failed,
        )


# Parser combinators.

class All(ParserCombinator):
    """
    All(ParserCombinator)

    Returns the concatenation of several parsers. If all of the
    parsers return a success, the concatenation returns a success
    with their individual results enumerated into a list. If any of
    the parsers return a failure, the concatenation does too.
    """

    def __call__(self, *parsers: Tuple[Parser]) -> Parser:
        assert len(parsers)

        def parser(parse: Parse) -> Parse:
            result = tuple() # Stores enumerated results.

            for parser in parsers:
                parse = parser(parse)

                if parse.failed:
                    return failure(parse)

                result += (parse.result, )

            return success(Parse(
                    string = parse.string,
                    result = result,
            ))

        return parser


class Any(ParserCombinator):
    """
    Any(ParserCombinator)

    Returns the alternation of several parsers. If any of the
    parsers return a success, the concatenation returns the first
    successful parse. Otherwise it returns a failure.
    """

    def __call__(self, *parsers: Tuple[Parser]) -> Parser:
        assert len(parsers)

        def parser(parse: Parse) -> Parse:

            for parser in parsers:
                new_parse = parser(parse)

                if not new_perse.failed:
                    return success(new_parse)

            return failure(parse)


class Maybe(ParserCombinator):
    """
    Maybe(ParserCombinator)

    Returns the optional equivalent of a given parser. Reduces to
    the alternation `Maybe(parse) = parse | Nothing`.
    """

    def __call__(self, *parsers: Tuple[Parser]) -> Parser:
        assert len(parsers) == 1

        return Any(parsers[0], Nothing)


class Many(ParserCombinator):
    """
    Many(ParserCombinator)

    Returns the plural of a given parser. Keeps applying the
    parser until it returns a failure. Returns the enuemrated
    results from successful parses.
    """

    def __call__(self, *parsers: Tuple[Parser]) -> Parser:
        assert len(parsers) == 1

        def parser(parse: Parse) -> Parse:
            result = tuple()

            while True:
                parse = parser[0](parse)

                if parse.failed:
                    return success(Parse(
                            string = parse.string,
                            result = result,
                    ))

                result += (parse.result, )
