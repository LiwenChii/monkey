import unittest
from .lexer import Lexer
from .token import Token, TokenType


class TestLexer(unittest.TestCase):
    def assert_token_equal(self, first, second):
        self.assertEqual(first._type, second._type)
        self.assertEqual(first._literal, second._literal)

    def test_next_token(self):
        input_str = '=+(){},;'
        l = Lexer(input_str)
        t = l.next_token()
        self.assert_token_equal(t, Token(TokenType.ASSIGN, '='))
