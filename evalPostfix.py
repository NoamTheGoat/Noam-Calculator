from customArithmeticOperations.digSumArthOpr import digit_sum
from customArithmeticOperations.minArthOpr import min_opr
from customArithmeticOperations.maxArthOpr import max_opr
from customArithmeticOperations.avgArthOpr import avg
from customArithmeticOperations.factorialArthOpr import factorial
from exceptionHandling import is_float
BIN_MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '$', '&', '@']
UN_MATH_OPERATORS = ['!', '#']

def eval_postfix(expression):
    """
        This function calculates a postfix notation expression, evaluates it using
        both binary and unary operators, and returns the calculated result.

        Parameters:
            expression (list): A list of operands and operators in postfix notation.

        Returns:
            float: The result of evaluating the expression.

        Raises:
            OverflowError: If the result exceeds allowable limits.
            ArithmeticError: If an invalid mathematical operation is encountered.
        """

    operand_list = []
    result = 0
    i=0
    while i < len(expression):
        c = expression[i]
        if is_float(c):
            operand_list.append(c)

        elif c in 'su':
            result = eval_un(float(operand_list.pop()), c)
            operand_list.append(result)

        elif c == '#':
            result = eval_un(operand_list.pop(), c)
            operand_list.append(result)

        elif c in BIN_MATH_OPERATORS:
            result = eval_bin(float(operand_list.pop()), c, float(operand_list.pop()))

            if result == float("inf"):
                raise OverflowError()
            operand_list.append(result)


        elif c in UN_MATH_OPERATORS:
            result = eval_un(float(operand_list.pop()), c)
            if result == float("inf"):
                raise OverflowError()

            operand_list.append(result)

        i+=1

    return operand_list.pop()


def eval_bin(operand2, operator, operand1):
    """
        Calculates a binary operation with two operands.

        Parameters:
            operand2 (float): The second operand.
            operator (str): The binary operator to be applied.
            operand1 (float): The first operand.

        Returns:
            float: The result of applying the binary operation.

        Raises:
            ArithmeticError: If an invalid mathematical operation is encountered.
        """
    if operator == '+':
        return operand1 + operand2

    elif operator == '-':
        return operand1 - operand2

    elif operator == '*':
        return operand1 * operand2

    elif operator == '/':
        if operand2==0:
            raise ArithmeticError("Cannot devide by 0")
        return operand1 / operand2

    elif operator == '^':
        if operand1<0 and operand2>-1 and operand2<1:
            raise ArithmeticError("Cannot do root to negative number")
        if operand2 == 0 and operand1 == 0:
            raise ArithmeticError("Cannot do power to 0^0")
        return operand1 ** operand2

    elif operator == '%':
        if operand2 == 0:
            raise ArithmeticError("Cannot devide by 0")
        return operand1 % operand2

    elif operator == '$':
        return max_opr(operand1, operand2)

    elif operator == '&':
        return min_opr(operand1, operand2)

    elif operator == '@':
        return avg(operand1, operand2)


def eval_un(operand, operator):
    """
        Evaluates a unary operation with a single operand.

        Parameters:
            operand (float): The operand.
            operator (str): The unary operator to be applied.

        Returns:
            float: The result of applying the unary operation.

        Raises:
            ArithmeticError: If an invalid mathematical operation is encountered.
            OverflowError: If the result exceeds allowable limits.
        """
    if operator == '!':
        if not operand == int(operand):
            raise ArithmeticError("Cannot do a factorial to a non whole number")
        if operand < 0:
            raise ArithmeticError("Cannot do a factorial to a negative number")
        if operand >170:
            raise OverflowError()
        if operand == 0:
            return 1
        return factorial(operand)

    elif operator == '#':
        return digit_sum(str(operand))

    elif operator == 'u' or operator == 's':  # Unary minus
        return -operand