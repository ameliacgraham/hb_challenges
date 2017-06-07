def calc(s):
    """
    >>> calc("+ 1 2")
    3
    >>> calc("* 2 + 1 2")
    6
    >>> calc("+ 9 * 2 3")
    15
    """

    tokens = s.split()
    operand2 = int(tokens.pop())
    while tokens:
        operand1 = int(tokens.pop())
        operator = tokens.pop()
        if operator == "+":
            operand2 = operand1 + operand2
        elif operator == "-":
            operand2 = operand1 - operand2
        elif operator == "*":
            operand2 = operand1 * operand2
        elif operator == "/":
            operand2 = operand1 / operand2
    return operand2

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"