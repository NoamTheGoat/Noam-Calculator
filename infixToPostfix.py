# Function to return precedence of operators
def prec(c):
    if c == 's':
        return 7
    if c == '!' or c == '#':
        return 6
    elif c == '@' or c == '&' or c == '$':
        return 5
    elif c == '%':
        return 4
    elif c == '^':
        return 3
    elif c=='u':
        return 2.5
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function to perform infix to postfix conversion
def infix_to_postfix(expression):
    st = []
    result = []
    i = 0

    while i < len(expression):
        c = expression[i]

        if is_number(c):
            result.append(c)

        elif c == '(':
            st.append('(')

        elif c == ')':
            while st and st[-1] != '(':
                result.append(st.pop())
            if st[-1] == 'u':
                result.append(st.pop())
            st.pop()

        else:
            while st and (prec(c) <= prec(st[-1])):
                result.append(st.pop())
            st.append(c)
        i += 1

    while st:
        result.append(st.pop())

    return result

