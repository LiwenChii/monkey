from enum import Enum, unique


@unique
class TokenType(Enum):
    ASSIGN = 0
    PLUS = 1
    LPAREN = 2
    RPAREN = 3
    LBRACE = 4
    RBRACE = 5
    COMMA = 6
    SEMICOLON = 7
    EOF = 8

    def __int__(self):
        return self.value

    def __repr__(self):
        template = 'TokenType.{}'
        return template.format(self.name)


class Token:
    def __init__(self, _type, literal):
        self._type = _type
        self._literal = literal

    def __repr__(self):
        template = 'Token({}, "{}")'
        return template.format(self._type, self._literal)
