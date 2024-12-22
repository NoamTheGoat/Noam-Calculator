def digit_sum(oprnd):
    """
        Calculates the sum of the digits of a positive number, raising exceptions in certain cases.

        Parameters:
            oprnd (str): The number, represented as a string, whose digits are to be summed.

        Returns:
            int: The sum of the digits of the input number.

        Raises:
            ArithmeticError: If the input contains 'e' (indicating a large number in scientific notation) or if the
                             input number is negative.
        """
    if "e" in oprnd:
        raise ArithmeticError("the number is to big to sum the digits")
    oprnd = oprnd.replace(".", "")
    sum = 0
    oprnd = int(oprnd)
    if oprnd < 0:
        raise ArithmeticError("cannot sum the digits of a negative number")
    while oprnd >= 1:
        sum += oprnd % 10
        oprnd //= 10

    return sum