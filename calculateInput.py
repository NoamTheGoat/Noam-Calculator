from buildNumbers import build_numbers
from customExceptions import SyntaxInputError
from exceptionHandling import legal_checking
from infixToPostfix import infix_to_postfix
from minusAndTildaHandling import minus_and_tilda_handling
from evalPostfix import eval_postfix

#def calculate(equastion):


if __name__ == "__main__":
    try:
        print("Welcome to my calculator!")
        print("\n---------------------------------------------------")
        equastion = input("Enter equation to calculate, enter omega to finish: ")


        while not equastion == "omega":
            try:
                equastion = "".join(equastion.split())
                eq_list = list(equastion)

                eq_list = build_numbers(eq_list)

                legal_checking(eq_list)

                eq_list = minus_and_tilda_handling(eq_list)

                eq_list = infix_to_postfix(eq_list)

                solution = eval_postfix(eq_list)

                print("The result is: "+str(solution))
                print("---------------------------------------------------\n")

            except OverflowError:
                print("The result is too big, try again")
                print("---------------------------------------------------\n")
            #except ArithmeticError as e:
            #    print(e, ", try again")
            #except SyntaxInputError as e:
            #    print(e, ", try again")
            except Exception as e:
                print(e, ", try again")
                print("---------------------------------------------------\n")

            print("---------------------------------------------------")
            equastion = input("Enter equastion to calculate, enter omega to finish: ")

    except KeyboardInterrupt:
        print("\n")

    print("Thanks for using my calculator, "
          "have a nice day and remember omega is the best!")
