class Program:
    def __init__(self):
        self.statements = []

    def token_literal(self):
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ''


class LetStatement:
    def __init__(self, token):
        self.token = token
        self.name = None
        self.value = None

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass


class Identifier:
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def token_literal(self):
        return self.token._literal