from customExceptions import SyntaxInputError
LEGAL_CHARACTERS = ["1234567890~!@#$%^&*()_+/"]
MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '$', '&', '@' '~', '!', '#']
BIN_MATH_OPERATORS = ['+', '*', '/', '^', '%', '$', '&', '@']
UN_MATH_OPERATORS = ['!', '#']

def legalChecking(expression):
    initialExceptionCheck(expression)
    parenthesesCheking(expression)
    operatorChecking(expression)


def initialExceptionCheck(expression):
    if not expression:
        raise SyntaxInputError("The input is empty")

    i=0
    while i < len(expression):
        c = expression[i]

        if c not in LEGAL_CHARACTERS:
            if c in ["[]{}<>"]:
                raise SyntaxInputError("The only parentheses allowed is () in position {}".format(i+1))
            else:
                raise SyntaxInputError("Illegal character in position {}".format(i+1))

def parenthesesCheking(expression):
    i = 0
    openCounter = 0
    closeCounter = 0

    while i < len(expression):
        c = expression[i]

        if c=="(":
            openCounter+=1
            if i+1<len(expression) and expression[i+1] == ")":
                raise SyntaxInputError("the parentheses content is empty")

        elif c==")":
            if closeCounter>=openCounter:
                if openCounter == 0:
                    raise SyntaxInputError("the first parentheses need to be ( in position {}".format(i+1))
                else:
                    raise SyntaxInputError("a ( cannot appear before ) in position {}".format(i+1))

def operatorChecking(expression): #after handling minus and tilda
    i=0
    if expression[0] in BIN_MATH_OPERATORS or expression[0] in UN_MATH_OPERATORS:
        raise SyntaxInputError("this operator {} cannot come at the beginning".format(expression[0]))

    if expression[-1] in BIN_MATH_OPERATORS or expression[-1] == '-':
        raise SyntaxInputError("this operator {} cannot come at the ending".format(expression[-1]))

    while i < len(expression):

        if i+1<len(expression) and expression[i] in BIN_MATH_OPERATORS:
            if expression[i+1] in BIN_MATH_OPERATORS or expression[i+1] in UN_MATH_OPERATORS:
                raise SyntaxInputError("this operator {} cannot come before {}".format(expression[i+1], expression[i]))

        elif i+1<len(expression) and expression[i] in UN_MATH_OPERATORS:
            if expression[i+1] == ")" or expression[i+1] == ".":
                raise SyntaxInputError("this character {} cannot come before {}".format(expression[i+1], expression[i]))

        elif i+1<len(expression) and expression[i] == "-":
            if not expression[i+1] in ["1234567890-("]:
                raise SyntaxInputError("this character {} cannot come before {}".format(expression[i+1], expression[i]))
