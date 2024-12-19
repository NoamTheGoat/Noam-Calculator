from customExceptions import SyntaxInputError
LEGAL_CHARACTERS = "~!@#$%^&*()-+/"
MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '$', '&', '@' '~', '!', '#']
BIN_MATH_OPERATORS = ['+', '*', '/', '^', '%', '$', '&', '@']
UN_MATH_OPERATORS = ['!', '#']

def legal_checking(expression):
    initial_exception_check(expression)
    parentheses_checking(expression)
    operator_checking(expression)


def initial_exception_check(expression):
    if not expression:
        raise SyntaxInputError("The input is empty")

    i=0
    while i < len(expression):
        c = expression[i]

        if not is_float(c):
            if c not in LEGAL_CHARACTERS:
                if c in "[]{}<>":
                    raise SyntaxInputError(""
                                           "The only parentheses allowed is () in position {}".format(i+1))
                else:
                    raise SyntaxInputError("Illegal character in the input")
        i+=1

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def parentheses_checking(expression):
    i = 0
    open_counter = 0
    close_counter = 0

    while i < len(expression):
        c = expression[i]

        if c=="(":
            open_counter+=1
            if i + 1 < len(expression) and expression[i+1] == ")":
                raise SyntaxInputError("the parentheses content is empty")
            if (i + 1 < len(expression) and
                    expression[i+1] in BIN_MATH_OPERATORS or expression[i+1] in UN_MATH_OPERATORS):
                raise SyntaxInputError(""
                                       "the operator {} cannot come after (".format(expression[i + 1]))

        elif c == ")":
            close_counter+=1
            if close_counter>open_counter:
                if i + 1 <len(expression) and expression[i+1].is_float:
                    raise SyntaxInputError(""
                                           "this operand {} cannot come after )".format(expression[i + 1], expression[i]))

                elif open_counter == 0:
                    raise SyntaxInputError(""
                                           "the first parentheses need to be ( in position {}".format(i+1))
                else:
                    raise SyntaxInputError(""
                                           "a ( cannot appear before ) in position {}".format(i+1))

        i += 1

    if open_counter>close_counter:
        raise SyntaxInputError("there are missing )".format(i + 1))


def operator_checking(expression):
    i=0
    if expression[0] in BIN_MATH_OPERATORS or expression[0] in UN_MATH_OPERATORS:
        raise SyntaxInputError(""
                               "this operator {} cannot come at the beginning".format(expression[0]))

    if expression[-1] in BIN_MATH_OPERATORS or expression[-1] == '-':
        raise SyntaxInputError(""
                               "this operator {} cannot come at the ending".format(expression[-1]))

    while i < len(expression):

        if i + 1 < len(expression) and expression[i] in BIN_MATH_OPERATORS:
            if (expression[i+1] in BIN_MATH_OPERATORS or
                    expression[i+1] in UN_MATH_OPERATORS):
                raise SyntaxInputError(""
                                       "this operator {} cannot come before {}".format(expression[i+1], expression[i]))

        elif i + 1 < len(expression) and expression[i] in UN_MATH_OPERATORS:
            if not (expression[i+1] == ")" or expression[i+1] in MATH_OPERATORS):
                raise SyntaxInputError(""
                                       "this character {} cannot come before {}".format(expression[i+1], expression[i]))

        elif i + 1 < len(expression) and expression[i] == "-":
            if not (is_float(expression[i+1]) or expression[i+1] in "1234567890-("):
                raise SyntaxInputError(""
                                       "this character {} cannot come before {}".format(expression[i+1], expression[i]))

        elif i > 0 and expression[i] == "~":
            if not (i == 0 or expression[i-1]
                    in BIN_MATH_OPERATORS or expression[i-1] == "(" or expression[i-1] == "-"):
                raise SyntaxInputError(""
                                       "this character {} cannot come before {}".format(expression[i-1], expression[i]))

        elif i + 1 < len(expression) and is_float(expression[i]):
            if expression[i+1] == "(":
                raise SyntaxInputError(""
                                       "this character {} cannot come before {}".format(expression[i+1], expression[i]))
        i += 1