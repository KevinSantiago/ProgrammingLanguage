from sympy import *


# method to derive equations based on variables passed to it
def newderivative(eq, *args):

    if len(args) == 0:
        eq = diff(eq)
    for sym in args:
        eq = diff(eq, sym)
    return eq


# new method to integrate definite/indefinite integrals depending on the parameters given
def newintegration(eq, *args):
    if len(args) == 0:
        eq = integrate(eq)
    for tups in args:
        eq = integrate(eq, tups)
    return eq


# method to change equation format; Not working for some reason
def formateq(eq):
    if isinstance(eq, str):
        tired = str(eq)
        tired.replace("^", "**")
        return tired


def summation(eq, lower, upper, sym):
    sumtotal = 0
    sumexpr = sympify(eq)
    while lower <= upper:
        newexpr = sumexpr.subs(sym, lower)
        sumtotal = sumtotal + newexpr
        lower += 1
    return sumtotal


def productnotation(eq, lower, upper, sym):
    prodtotal = 1
    sumexpr = sympify(eq)
    while lower <= upper:
        newexpr = sumexpr.subs(sym, lower)
        prodtotal = prodtotal * newexpr
        lower += 1
    return prodtotal


# Method to evaluate limits; can evaluate from one side
def limits(eq, sym, sym0, side=None):
    if side is None:
        return limit(eq, sym, sym0)
    else:
        return limit(eq, sym, sym0, side)


print("derivations testing\n")
# parameters: equation, *symbols
print(newderivative('1/(x**2)'))
# If there's more than one variable in the exp, the variable(s) of differentiation must be supplied to differentiate
print(newderivative('4*x**2*y**2', symbols('x')))
print('\nIntegrating testing\n')
# parameters: equation, *symbols
print('indefinite integral ', newintegration('2*x'))
# parameters: equation, *tuple(symbol, lowerbound, upperbound)
print('definite integral ', newintegration('2*x', (symbols('x'), 0, 2)))

# If the integrand contains more than one free symbol, an integration variable should be supplied explicitly
# parameters: equation, *symbols
print('indefinite integral ', newintegration('2*x**2*y + 2*x*y**2', symbols('x'), symbols('y')))
# parameters: equation, *tuple(symbol, lowerbound, upperbound)
print('definite integral ', newintegration('2*x**2*y + 2*x*y**2', (symbols('x'), 0, 2), (symbols('y'), 0, 2)))

# variable to be replaced must be initialized as a symbol and sent as a parameter for these methods to work
# parameters: equation, lowerbound, upperbound, symbol
print('\ntesting summation\n')
print(summation('x**2', 0, 6, symbols('x')))

print('\ntesting product notation\n')
print(productnotation('x**2', 1, 6, symbols('x')))

print('\ntesting limits\n')
# parameters: equation, x, x0, side to evaluate
print(limits('1/x', symbols('x'), 0, '+'))
print(limits('sin(x)/x', symbols('x'), 0))
# testing string replacing for exponent
print('\ntesting formatting\n')
str1 = "4x^2"
print(str1.replace("^", "**"))
print(formateq("4x^2"))
