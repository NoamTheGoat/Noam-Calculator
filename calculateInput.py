from buildNumbers import buildNumbers
from infixToPostfix import infixToPostfix
from minusAndTildaHandling import minusAndTildaHandling
from evalPostfix import evalPostfix

def calculate(equastion):

    equastion = "".join(equastion.split())
    eq_list = list(equastion)

    #legalCharacters(eq_list)
    #otherErrorChecks

    #minusAndTildaErrorCheck(eq_List)

    eq_list = buildNumbers(eq_list)

    eq_list =  minusAndTildaHandling(eq_list)

    #infixToPostfixErrorCheck(eq_List)

    eq_list = infixToPostfix(eq_list)

    solution = evalPostfix(eq_list)

    return solution

print(calculate("4--------4-4"))