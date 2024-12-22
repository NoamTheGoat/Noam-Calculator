from customExceptions import SyntaxInputError
from exceptionHandling import is_float

MATH_OPERATORS = ['+', '-', '*', '/', '^', '%', '~', '(']

def minus_and_tilda_handling(input_list):
    """
        Processes and handles the special cases for the minus '-' and tilde '~' operators in the input list.
        The function handles the reduction of consecutive minus and tilde operators, and applies the appropriate
        transformations to the operands.

        Parameters:
            input_list (list): A list of strings representing the expression, where each string is a character or operator.

        Returns:
            list: A list of strings where the tilde and minus operators are handled appropriately.
        """
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
                    is_tilda_minus = False
            else:
                result.append(c)

        elif c in MATH_OPERATORS:
            result.append(c)

        else:
            result.append(c)
        i += 1

    return result

def minus_or_tilda_reduction(input_list, index = 0):
    """
        Processes the input list starting at the given index to handle consecutive minus '-' and tilde '~' operators.
        The function will reduce consecutive minus and tilde operators.
        Parameters:
            input_list (list): A list of strings representing the expression.
            index (int): The index to start processing from (default is 0).

        Returns:
            int: The updated index after processing the minus or tilde operators.

        Raises:
            SyntaxInputError: If a minus or tilde operator appears in an invalid position.
        """
    i = index
    if input_list[i] == '~':
        i += 1
    while input_list[i] == '-':
        i += 1
    if not (is_float(input_list[i]) or input_list[i]=="(" or
            (index > 0 and input_list[index-1] == '-')):
        raise SyntaxInputError("- cannot come before ~")
    return i
