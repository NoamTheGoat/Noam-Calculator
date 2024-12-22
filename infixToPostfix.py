# Function to return precedence of operators
from exceptionHandling import is_float


def prec(c):
    """
        Determines the precedence of a given operator.

        Parameters:
            c (str): The operator whose precedence is to be determined.

        Returns:
            int: The precedence of the operator.
        """
    if c == 's':
        return 7
    if c == '!' or c == '#':
        return 6
    elif c == '@' or c == '&' or c == '$':
        return 5
    elif c == '%':
        return 4
    elif c == '^':
        return 3
    elif c=='u':
        return 2.5
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

# Function to perform infix to postfix conversion
def infix_to_postfix(expression):
    """
       Converts an infix mathematical expression to a postfix expression.

       Parameters:
           expression (str): The mathematical expression in infix notation, represented as a string.

       Returns:
           list: A list representing the postfix expression, where operators come after their operands.
       """
    st = []
    result = []
    i = 0

    while i < len(expression):
        c = expression[i]

        if is_float(c):
            result.append(c)

        elif c == '(':
            st.append('(')

        elif c == ')':
            while st and st[-1] != '(':
                result.append(st.pop())
            if st[-1] == 'u':
                result.append(st.pop())
            st.pop()

        else:
            while st and (prec(c) <= prec(st[-1])):
                result.append(st.pop())
            st.append(c)
        i += 1

    while st:
        result.append(st.pop())

    return result

