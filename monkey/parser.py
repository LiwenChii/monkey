from .token import Token, TokenType
from .ast import Program, LetStatement, Identifier


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.cur_token = Token(TokenType.EOF, '')
        self.peek_token = Token(TokenType.EOF, '')

        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def expect_peek(self, token_type):
        if self.peek_token_is(token_type):
            self.next_token()
            return True
        else:
            return False

    def peek_token_is(self, token_type):
        return self.peek_token._type == token_type

    def cur_token_is(self, token_type):
        return self.cur_token._type == token_type

    def parse_program(self):
        program = Program()

        while self.cur_token._type != TokenType.EOF:
            statement = self.parse_statement()
            program.statements.append(statement)

            self.next_token()

        return program

    def parse_statement(self):
        if self.cur_token._type == TokenType.LET:
            return self.parse_let_statement()
        else:
            return None

    def parse_let_statement(self):
        statement = LetStatement(self.cur_token)

        if not self.expect_peek(TokenType.IDENT):
            return None

        statement.name = Identifier(self.cur_token, self.cur_token._literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None

        while not self.expect_peek(TokenType.SEMICOLON):
            self.next_token()

        return statement
