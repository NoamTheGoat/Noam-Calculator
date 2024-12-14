from customArithmeticOperations.minArthOpr import minOpr
from customArithmeticOperations.maxArthOpr import maxOpr
from customArithmeticOperations.avgArthOpr import avgOpr
from customArithmeticOperations.factorialArthOpr import factorialOpr

BIN_MATH_OPERATORS = ['+', '-', '*', '/', '^', '%']
UN_MATH_OPERATORS = ['!']
def evalPostfix(expression):
    operand_list = []
    i=0
    while i < len(expression):
        c = expression[i]
        if c.isdigit():
            operand_list.append(int(c))

        #check if '-' is unary minus
        elif c == '-' and (i+1==len(expression) or expression[i+1] in BIN_MATH_OPERATORS or expression[i+1] in UN_MATH_OPERATORS):
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
        return operand1 / operand2
    elif operator == '^':
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
        return factorialOpr(operand)
    elif operator == '-':
        return -1*operand