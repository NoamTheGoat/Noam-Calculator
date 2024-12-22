from buildNumbers import build_numbers
from customExceptions import SyntaxInputError
from exceptionHandling import legal_checking
from infixToPostfix import infix_to_postfix
from minusAndTildaHandling import minus_and_tilda_handling
from evalPostfix import eval_postfix

def calculate(equastion):
    """
        Processes a mathematical equation string and calculates the result.
        This function takes a string representation of a mathematical equation,
        parses it, validates its syntax, converts it to postfix, and evaluates it.

        Parameters:
            equastion (str): The mathematical equation to be evaluated.

        Returns:
            float: The result of the mathematical equation.

        Raises:
            SyntaxInputError: If the equation contains invalid syntax.
            OverflowError: If the result is too big.
            Exception: For other errors encountered during processing.
        """
    equastion = "".join(equastion.split())
    eq_list = list(equastion)

    eq_list = build_numbers(eq_list)

    legal_checking(eq_list)

    eq_list = minus_and_tilda_handling(eq_list)

    eq_list = infix_to_postfix(eq_list)

    solution = eval_postfix(eq_list)
    return solution


if __name__ == "__main__":
    try:
        print("Welcome to my calculator!")
        print("\n----------------------------------------------------------------------------")
        equastion = input("Enter equation to calculate, "
                          "enter h for help and goodbye/quit/exit to exit: ")


        while not equastion in ["goodbye", "quit", "exit"]:
            try:
                if equastion in ["h", "help"]:
                    print("manual:\n"
                          "addition : X+X\n"
                          "subtraction : X-X\n"
                          "multiplication : X*X\n"
                          "division : X/X\n"
                          "power : X^X\n"
                          "modulo: X%X\n"
                          "maximum: X$X\n"
                          "minimum: X&X\n"
                          "average: X@X\n"
                          "negate: ~X\n"
                          "factorial: X!\n"
                          "sum of digits: X#")
                    print("----------------------------------------------------------------------------\n")


                else:
                    solution = calculate(equastion)
                    print("The result is: " + str(solution))
                    print("----------------------------------------------------------------------------\n")

            except OverflowError:
                print("The result is too big, try again")
                print("----------------------------------------------------------------------------\n")
            #except ArithmeticError as e:
            #    print(e, ", try again")
            #except SyntaxInputError as e:
            #    print(e, ", try again")
            except Exception as e:
                print(e, ", try again")
                print("----------------------------------------------------------------------------\n")

            print("----------------------------------------------------------------------------")
            equastion = input("Enter equation to calculate, "
                              "enter h for help and goodbye/quit/exit to exit: ")
    except KeyboardInterrupt:
        print("\n")

    print("Thanks for using my calculator, "
          "have a nice day and remember omega is the best!")
