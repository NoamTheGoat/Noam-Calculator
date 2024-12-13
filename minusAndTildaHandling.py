MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '~', '!', '(', ')']
MATH_OPERATORS_ABOVE_UNARY_MINUS = ['^', '%', '~', '!']

def minusAndTildaHandling(list):
    result = []
    temp_index = 0
    is_unary_minus = False

    if list[0] == '~':
        temp_index = minusOrTildaReduction(list)
        if temp_index % 2 == 1:
            result.append('-')


    elif list[0] == '-':
        temp_index = minusOrTildaReduction(list)
        if temp_index % 2 == 1:
            result.append('-')

        temp_ptr_index = temp_index + 1
        if  temp_ptr_index < len(list) and list[temp_ptr_index] in MATH_OPERATORS_ABOVE_UNARY_MINUS:
            is_unary_minus = True

    i = temp_index
    while i < len(list):
        c = list[i]

        if c == '~' or (c == '-' and (list[i - 1] in MATH_OPERATORS)):
            tIndex=minusOrTildaReduction(list, i)
            if (tIndex - i) % 2 == 1:
                result.append('-')
            i = tIndex - 1

        elif c.isdigit():  # Includes negative numbers
            if result and result[-1] == '-' and not is_unary_minus:
                result[-1] = '-' + c
            else:
                is_unary_minus = False
                result.append(c)

        elif c in MATH_OPERATORS:
            result.append(c)

        else: #check if legal character
            result.append(c)
        i+=1

    return result

def minusOrTildaReduction(list, index = 0):
    i = index
    if list[i]== '~':
        i+=1
    while list[i]== '-':
        i+=1
    #if(list[i] >= '0' and list[i] <= '9'): #check if i finished the list
    return i

print(minusAndTildaHandling(["-", "5"]))
print(minusAndTildaHandling(["-", "5", "!"]))
print(minusAndTildaHandling(["~","(", "2", "-", "-", "555","!",")"]))