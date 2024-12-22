from customExceptions import SyntaxInputError


def build_numbers(expression):
    """
        This function processes a list of characters representing a mathematical
        expression and groups sequences of digits into a number
        (and a possible decimal point) into full numbers.

        Parameters:
            expression (list): A list of characters representing a mathematical expression.

        Returns:
            list: A list where sequences of numeric characters are combined into strings
            representing numbers, and all other characters remain unchanged.

        Raises:
            SyntaxInputError: If an invalid number is detected in the input.
        """
    result = []

    i=0
    while i < len(expression):
        c = expression[i]

        if c.isdigit():
            num = ''
            while (i < len(expression) and
                   (expression[i].isdigit() or expression[i]=='.')):

                num+=expression[i]
                i+=1
            try:
                tmpnum = float(num)
            except ValueError:
                raise SyntaxInputError(""
                                       "The number {} is not legal in in position".format(num))
            result.append(num)
            continue
        else:
            result.append(c)
        i+=1
    return result