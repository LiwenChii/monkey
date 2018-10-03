from .token import Token, TokenType


class Lexer:
    def __init__(self, input_str):
        self.ch = ''
        self.position = 0
        self.read_position = 0
        self.input_str = input_str
        self._keyword_map = {
            'fn': TokenType.FUNCTION,
            'let': TokenType.LET,
        }

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
        elif self.is_letter(self.ch):
            ident = self.read_identifier()
            ident_type = self.look_up_ident_type(ident)
            return Token(ident_type, ident)
        else:
            return Token(TokenType.EOF, '')

    def read_char(self):
        if self.read_position >= len(self.input_str):
            self.ch = ''
        else:
            self.ch = self.input_str[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def read_identifier(self):
        position = self.position
        while self.is_letter(self.ch):
            self.read_char()

        return self.input_str[position:self.position]

    def look_up_ident_type(self, identifier):
        ident_type = self._keyword_map.get(identifier)
        if ident_type is None:
            return TokenType.IDENT
        return ident_type

    @staticmethod
    def is_letter(ch):
        letters = [chr(i) for i in range(97, 123)]
        capital_letters = [chr(i).upper() for i in range(97, 123)]
        letter_list = letters + capital_letters + ['_']

        return ch in letter_list
