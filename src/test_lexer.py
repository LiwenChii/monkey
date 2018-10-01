import unittest
from .lexer import Lexer


class TestLexer(unittest.TestCase):
    def test_next_token(self):
        input_str = '=+(){},;'
        l = Lexer(input_str)
        t = l.next_token()
        self.assertEqual(t, ('equal', '='))
