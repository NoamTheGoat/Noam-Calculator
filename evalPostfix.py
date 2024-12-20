from customArithmeticOperations.digSumArthOpr import digit_sum
from customArithmeticOperations.minArthOpr import min_opr
from customArithmeticOperations.maxArthOpr import max_opr
from customArithmeticOperations.avgArthOpr import avg
from customArithmeticOperations.factorialArthOpr import factorial
from infixToPostfix import is_number
BIN_MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '$', '&', '@']
UN_MATH_OPERATORS = ['!', '#']

def eval_postfix(expression):
    operand_list = []
    result = 0
    i=0
    while i < len(expression):
        c = expression[i]
        if is_number(c):
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