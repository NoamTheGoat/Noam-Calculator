from buildNumbers import buildNumbers
from hastagHandling import hastagHandling
from infixToPostfix import infixToPostfix
from minusAndTildaHandling import minusAndTildaHandling
from evalPostfix import evalPostfix

def calculate(equastion):

    equastion.strip()
    eq_list = list(equastion)

    #legalCharacters(eq_list)
    #otherErrorChecks
    #hastagErrorCheck(eq_List)

    #eq_list = hastagHandling(eq_list)

    #minusAndTildaErrorCheck(eq_List)

    eq_list = buildNumbers(eq_list)

    eq_list =  minusAndTildaHandling(eq_list)

    #infixToPostfixErrorCheck(eq_List)

    eq_list = infixToPostfix(eq_list)

    solution = evalPostfix(eq_list)

    return solution

print(calculate("1234.5#"))