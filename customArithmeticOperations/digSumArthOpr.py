
def digit_sum(oprnd):
    oprnd = oprnd.replace(".", "")
    sum = 0
    oprnd = int(oprnd)
    if oprnd < 0:
        raise ArithmeticError("cannot sum the digits of a negative number")
    while oprnd >= 1:
        sum += oprnd % 10
        oprnd //= 10

    return sum