from .token import Token, TokenType


class Lexer:
    def __init__(self, input_str):
        self.ch = ''
        self.position = 0
        self.read_position = 0
        self.input_str = input_str

    def next_token(self):
        self.read_char()

        if self.ch == '=':
            return Token(TokenType.ASSIGN, '=')
        elif self.ch == '+':
            return Token(TokenType.PLUS, '+')
        elif self.ch == ',':
            return Token(TokenType.COMMA, ',')
        elif self.ch == '(':
            return Token(TokenType.LPAREN, '(')
        elif self.ch == ')':
            return Token(TokenType.RPAREN, ')')
        elif self.ch == '{':
            return Token(TokenType.LBRACE, '{')
        elif self.ch == '}':
            return Token(TokenType.RBRACE, '}')
        elif self.ch == ';':
            return Token(TokenType.SEMICOLON, ';')
        else:
            return Token(TokenType.EOF, '')

    def read_char(self):
        if self.read_position >= len(self.input_str):
            self.ch = ''
        else:
            self.ch = self.input_str[self.read_position]
            self.position = self.read_position
            self.read_position += 1
