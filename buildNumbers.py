from customExceptions import SyntaxInputError


def build_numbers(expression):
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