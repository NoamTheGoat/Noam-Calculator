from customArithmeticOperations.digSumArthOpr import digSumArthOpr
from customArithmeticOperations.minArthOpr import minOpr
from customArithmeticOperations.maxArthOpr import maxOpr
from customArithmeticOperations.avgArthOpr import avgOpr
from customArithmeticOperations.factorialArthOpr import factorialOpr
from infixToPostfix import is_number

BIN_MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '$', '&', '@']
UN_MATH_OPERATORS = ['!', '#']
def evalPostfix(expression):
    operand_list = []
    i=0
    while i < len(expression):
        c = expression[i]
        if is_number(c):
            operand_list.append(float(c))

        #check if '-' is unary minus
        elif c == 'u':
            result = evalUn(operand_list.pop(), c)
            operand_list.append(result)

        elif c in BIN_MATH_OPERATORS:
            result = evalBin(operand_list.pop(), c, operand_list.pop())
            operand_list.append(result)

        elif c in UN_MATH_OPERATORS:
            result = evalUn(operand_list.pop(), c)
            operand_list.append(result)

        i+=1

    return operand_list.pop()

def evalBin(operand2, operator, operand1):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if(operand2==0):
            raise ArithmeticError("Cannot devide by 0")
        return operand1 / operand2
    elif operator == '^':
        if operand1<0 and operand2>-1 and operand2<1:
            raise ArithmeticError("Cannot do squirt to negative number.")
        return operand1 ** operand2
    elif operator == '%':
        return operand1 % operand2
    elif operator == '$':
        return maxOpr(operand1, operand2)
    elif operator == '&':
        return minOpr(operand1, operand2)
    elif operator == '@':
        return avgOpr(operand1, operand2)

def evalUn(operand, operator):
    if operator == '!':
        if not operand == int(operand):
            raise ArithmeticError("Cannot do a factorial to a non negative number.")
        if operand < 0:
            raise ArithmeticError("Cannot do a factorial to a negative number.")
        if operand >170:
            raise OverflowError()
        return factorialOpr(operand)
    elif operator == '#':
        if operand < 0:
            raise ArithmeticError("Cannot sum the digits of a negative number.")
        return digSumArthOpr(operand)
    elif operator == 'u':  # Unary minus
        return -operand