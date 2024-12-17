from customExceptions import SyntaxInputError


def buildNumbers(expression):
    result = []

    i=0
    while i < len(expression):
        c = expression[i]

        if c.isdigit():
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i]=='.'):
                num+=expression[i]
                i+=1

            try:
                num = float(num)
            except ValueError:
                raise SyntaxInputError("The number is not legal in in position {}".format(i))
            num = str(num)
            result.append(num)
            continue

        else:
            result.append(c)
        i+=1
    return result