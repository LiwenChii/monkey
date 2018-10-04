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
        self.read_char()

    def next_token(self):
        self.skip_white_space()

        if self.ch == '=':
            tk = Token(TokenType.ASSIGN, '=')
        elif self.ch == '+':
            tk = Token(TokenType.PLUS, '+')
        elif self.ch == ',':
            tk = Token(TokenType.COMMA, ',')
        elif self.ch == '(':
            tk = Token(TokenType.LPAREN, '(')
        elif self.ch == ')':
            tk = Token(TokenType.RPAREN, ')')
        elif self.ch == '{':
            tk = Token(TokenType.LBRACE, '{')
        elif self.ch == '}':
            tk = Token(TokenType.RBRACE, '}')
        elif self.ch == ';':
            tk = Token(TokenType.SEMICOLON, ';')
        elif self.is_letter(self.ch):
            token_literal = self.read_identifier()
            token_type = self.look_up_ident_type(token_literal)
            return Token(token_type, token_literal)
        elif self.ch.isdigit():
            token_literal = self.read_number()
            token_type = TokenType.INT
            return Token(token_type, token_literal)
        elif self.ch == '':
            tk = Token(TokenType.EOF, '')
        else:
            tk = Token(TokenType.ILLEGAL, self.ch)

        self.read_char()
        return tk

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

    def read_number(self):
        position = self.position

        while self.ch.isdigit():
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

    def skip_white_space(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.read_char()
