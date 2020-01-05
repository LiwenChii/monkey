from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    @abstractmethod
    def token_literal(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Program(Node):
    def __init__(self):
        self.statements = []

    def token_literal(self):
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ''

    def __str__(self):
        r = ''
        for s in self.statements:
            r += str(s)
        return r


class LetStatement(Node):
    def __init__(self, token):
        self.token = token
        self.name = None
        self.value = None

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass

    def __str__(self):
        s = '{} {} = {};'.format(self.token_literal(), self.name, self.value)
        return s


class Identifier(Node):
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def token_literal(self):
        return self.token._literal

    def __str__(self):
        return self.value


class ReturnStatement:
    def __init__(self, token):
        self.token = token
        self.value = None

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass

    def __str__(self):
        s = '{} {};'.format(self.token_literal(), self.value)
        return s


class ExpressionStatement:
    def __init__(self, token):
        self.token = token
        self.expression = None

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass

    def __str__(self):
        return str(self.expression)


class IntegerLiteral:
    def __init__(self, token):
        self.token = token
        self.value = None

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass

    def __str__(self):
        return self.token_literal()


class PrefixExpression:
    def __init__(self, token, operator):
        self.token = token
        self.operator = operator
        self.right = None

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass

    def __str__(self):
        s = '({}{})'.format(self.operator, str(self.right))
        return s


class InfixExpression:
    def __init__(self, token, operator, left):
        self.token = token
        self.left = left
        self.operator = operator
        self.right = None

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass

    def __str__(self):
        s = '({} {} {})'.format(str(self.left), self.operator, str(self.right))
        return s


class Boolean:
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def token_literal(self):
        return self.token._literal

    def statement_node(self):
        pass

    def __str__(self):
        return self.token_literal()