import pytest
from calculateInput import calculate
from customExceptions import SyntaxInputError


def test_simple_syntax_error():
    simple_syntax_error = ["3++5",
                           "3^*2",
                           "123#3",
                           "1~1",
                           "(3+4"]
    for equ in simple_syntax_error:
        with pytest.raises(SyntaxInputError):
            calculate(equ)


def test_gibberish_input():
    with pytest.raises(SyntaxInputError):
        calculate("omega")


def test_empty_input():
    with pytest.raises(SyntaxInputError):
        calculate("")


def test_white_spaces_input():
    white_spaces_input = [" ",
                          "     ",
                          "                 "]
    for equ in white_spaces_input:
        with pytest.raises(SyntaxInputError):
            calculate(equ)


def test_simple_equations():
    simple_equations = [("2 ^ 3", 8),
                        ("10 % 3", 1),
                        ("3 $ 5", 5),
                        ("3 & 5", 3),
                        ("3 @ 4", 3.5),
                        ("~5", -5),
                        ("5!", 120),
                        ("0!", 1),
                        ("(2 + 3) * 4", 20),
                        ("-5 + 3", -2),
                        ("~(-3)", 3),
                        ("3 + 2 * 4", 11),
                        ("10 / 3", 10 / 3) ]
    for equ, res in simple_equations:
        assert float(calculate(equ)) == res


def test_complex_equations():
    complex_equations = [("((3 + 5) * (2 ^ 3)-   4)/(7 + 1) ^ 2 % 5", 0.9375),
                         ("((5 + 3) * (4 ^ 2) %  7) + (9 $ 2) - 4", 21),
                         ("3 * 2 +   5 - 3 ^ 2 * 7 / 3 %   4 + 6 - 2", -6),
                         ("3 * (2 + (5 - 3) ^   2) -(-(-(4)))", 14),
                         ("((2 *   3) + (4 ^ 2)) $ 2 - (9 @ 2)", 16.5),
                         ("(3 * 2) @ (4 + 6) / (3 % 2) + (7!-5)", 5043),
                         ("(7 + 2 * 3) / (5 % 3 ) + 2! & 6+4@2", 11.5),
                         ("((2 ^ (3   + 2)) - (3 * (5 - 1))) / (4 + (2 * (3 - 1)))", 2.5),
                         ("((6 * 3) - (2 ^ 3)) + (4 / (5 - 3))", 12),
                         ("(7.5 + 3.2)*(2.5 -   1.5)/(4.8 + 1.2)-(5.3   * 2.0)+(6.5 / 3.5)",  -6.959523809523809),
                         ("((3.2 *    4.5) + (6.7 - 2.3) ^ 2) / (5.0 + 2.5) - 3.8 + (4.5 / 3.0)", 2.2013333333333343),
                         ("((10 - (2 * (5 + 3)))   + 6) ^ ((3 + 4) * 2) - 3", -3),
                         ("((3 ^ 2) - 5) *    (7 + 2) / (8 - 3)", 7.2),
                         ("((7 + (2 * (3 + 5)  ) ) - (5 ^ 2)) * ((6 + (3 - 2)) ^ 2)", -98),
                         ("999999999999.999999999999999999999999999999999999999999999999#", 540)]
    for equ, res in complex_equations:
        assert float(calculate(equ)) == res

def test_big_result_error():
    big_result = ["200!",
                  "10^100 * 10^100 * 10^100 * 10^100 * 10^100 * 10^100 * 10^100",
                  "9999^100000000000000000000000000"]
    for equ in big_result:
        with pytest.raises(OverflowError):
            calculate(equ)

def test_arithmetic_errors():
    arithmetic_errors = ["10/0",
                         "(10 ^ 2 / 5) % (6^2-36)",
                         "5--5^0.5",
                         "~4!",
                         "(9/4)!",
                         "0^0"]
    for equ in arithmetic_errors:
        with pytest.raises(ArithmeticError):
            calculate(equ)