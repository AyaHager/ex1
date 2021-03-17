def factorial(x):
    fact = 1
    for j in range(1, x + 1):
        fact = fact * j
    return fact


def exponent(x):
    expx = 1
    copyX = x
    for i in range(1, 80):
        expx = expx + (x / factorial(i))
        x = x * copyX
    return expx


def abs(x):
    if x < 0:
        x = -x
    return x


def ln(x):
    if x <= 0:
        return 0
    yn = 0
    yn1 = x - 1.0
    epsilon = 0.001
    while abs(yn - yn1) > epsilon:
        yn = yn1
        yn1 = yn + 2 * ((x - exponent(yn)) / (x + exponent(yn)))
    return yn1


def XtimesY(x: float, y: float):
    if x<=0:
        return 0
    else:
        return exponent(y * ln(x))


def sqrt(x: float, y: float):
    if x != 0 and y >= 0:
        return XtimesY(x, 1 / y)
    else:
        return 0


def calculate(x: float):
    return float(exponent(x)) * float(XtimesY(7, x)) * float(XtimesY(x, -1)) * float(sqrt(x, x))


if __name__ == '__main__':
    x = float(input("insert a number please\n"))
    print(calculate(x))
