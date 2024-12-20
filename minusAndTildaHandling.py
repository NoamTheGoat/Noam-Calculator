from customExceptions import SyntaxInputError
from exceptionHandling import is_float

MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '~', '(']

def minus_and_tilda_handling(input_list):
    result = []
    temp_index = 0
    is_tilda_minus = False
    is_sign_minus = False


    if input_list[0] == '~':
        temp_index = minus_or_tilda_reduction(input_list)
        if temp_index % 2 == 1:
            result.append('s')
            is_tilda_minus = True

    elif input_list[0] == '-':
        temp_index = minus_or_tilda_reduction(input_list)
        if temp_index % 2 == 1:
            result.append('u')

    i = temp_index
    while i < len(input_list):
        c = input_list[i]

        if c == '~' or (c == '-' and (input_list[i - 1] in MATH_OPERATORS)):
            if c == '~':
                is_tilda_minus = True
                if i + 1 < len(input_list) and input_list[i+1] == "(":
                    temp_index = minus_or_tilda_reduction(input_list, i)
                    if (temp_index - i) % 2 == 1:
                        result.append('s')
                else:
                    temp_index = minus_or_tilda_reduction(input_list, i)
                    if (temp_index - i) % 2 == 1:
                        result.append('-')

            elif result[-1] == '(':
                temp_index = minus_or_tilda_reduction(input_list, i)
                if (temp_index - i) % 2 == 1:
                    result.append('u')

            else:
                is_sign_minus = True
                temp_index = minus_or_tilda_reduction(input_list, i)
                if i + 1 < len(input_list) and input_list[i + 1] == "(":
                    if (temp_index - i) % 2 == 1:
                        result.append('s')
                else:
                    if (temp_index - i) % 2 == 1:
                        result.append('-')

                i = temp_index - 1


        elif is_float(c):
            if result:
                if result[-1] == '-' and is_sign_minus:
                    result[-1] = '-' + c
                elif is_tilda_minus and (result[-1] == 's' or result[-1]=='-'):
                    result[-1] = '-' + c
                else:
                    result.append(c)
            else:
                result.append(c)

        elif c in MATH_OPERATORS:
            result.append(c)

        else: #check if legal character
            result.append(c)
        i += 1

    return result

def minus_or_tilda_reduction(input_list, index = 0):
    i = index
    if input_list[i] == '~':
        i += 1
    while input_list[i] == '-':
        i += 1
    if not (is_float(input_list[i]) or input_list[i]=="(" or
            (index > 0 and input_list[index-1] == '-')):
        raise SyntaxInputError("- cannot come before ~")
    return i
