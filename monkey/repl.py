from lexer import Lexer
from token import TokenType


def start():
    prompt = '>> '
    while True:
        str_input = input(prompt)
        l = Lexer(str_input)
        token = l.next_token()
        while token._type != TokenType.EOF:
            print(token)
            token = l.next_token()
