from buildNumbers import buildNumbers
from infixToPostfix import infixToPostfix
from exceptionHandling import *
from minusAndTildaHandling import minusAndTildaHandling
from evalPostfix import evalPostfix

def calculate(equastion):

    equastion = "".join(equastion.split())
    eq_list = list(equastion)

    #legalCharacters(eq_list)
    #otherErrorChecks

    #minusAndTildaErrorCheck(eq_List)
    try:
        legalChecking(eq_list)


        eq_list = buildNumbers(eq_list)

        eq_list =  minusAndTildaHandling(eq_list)

    #infixToPostfixErrorCheck(eq_List)

        eq_list = infixToPostfix(eq_list)

        solution = evalPostfix(eq_list)
    except OverflowError:
        print("The expression of the equation is to big to calculate")
    except Exception as e:
        print(e)

    return solution

print(calculate("3++3"))