def buildNumbers(expression):
    result = []

    i=0
    while i < len(expression):
        c = expression[i]

        if c.isdigit():
            num = c
            while i+1<len(expression) and expression[i + 1].isdigit(): #i + 1 < len(s) and
                i += 1
                num += expression[i]
            if expression[i+1]=='.':
                i += 1
                num += expression[i]
                while i + 1 < len(expression) and expression[i + 1].isdigit():  # i + 1 < len(s) and
                    i += 1
                    num += expression[i]
            result.append(num)

        else:
            result.append(c)

        i+=1

    return result