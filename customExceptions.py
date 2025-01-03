class SyntaxInputError(Exception):
    """
    A custom exception for invalid syntax errors

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#class ArithmeticError(exc)