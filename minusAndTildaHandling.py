MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '~', '!', '(']

def minusAndTildaHandling(input_list):
    result = []
    temp_index = 0
    #is_unary_minus = False
    is_sign_minus = False
    if input_list[0] == '~':
        temp_index = minusOrTildaReduction(input_list)
        if temp_index % 2 == 1:
            result.append('-')

    elif input_list[0] == '-':
        temp_index = minusOrTildaReduction(input_list)
        if temp_index % 2 == 1:
            result.append('u')

    i = temp_index
    while i < len(input_list):
        c = input_list[i]

        if c == '~' or (c == '-' and (input_list[i - 1] in MATH_OPERATORS)):
            if result[-1] == '(':
                tIndex = minusOrTildaReduction(input_list, i)
                if (tIndex - i) % 2 == 1:
                    result.append('u')
            else:
                is_sign_minus = True
                tIndex=minusOrTildaReduction(input_list, i)
                if (tIndex - i) % 2 == 1:
                    result.append('-')
                i = tIndex - 1

        elif c.isdigit():
            if result and (result[-1] == '-' and is_sign_minus): # and not is_unary_minus:
                result[-1] = '-' + c
            else:
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

#print(minusAndTildaHandling(["-", "5", "#"]))
#print(minusAndTildaHandling(["-", "5", "!"]))
#print(minusAndTildaHandling(["~","(", "-", "2", "-", "-", "555","!",")"]))