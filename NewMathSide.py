from sympy import *
# ALL VARIABLES USED IN EQUATIONS MUST BE DECLARED AS SYMBOLS OR ELSE SYMPY METHODS WILL NOT RECOGNIZE THEM
x, y, z, t =0

def symbolsConversion(x1,y1,z1,t1):
   global x
   x = symbols(x1)
   global y
   y = symbols(y1)
   global z
   z = symbols(z1)
   global t
   t = symbols(t1)



# method to derive equation based on variables present
def derivative(eq):
    x_value = 0
    y_value = 0
    z_value = 0
    if 'x' in eq:
        x_value = 1
    if 'y' in eq:
        y_value = 1
    if 'z' in eq:
        z_value = 1

    return diff(eq, x, x_value, y, y_value, z, z_value)


# method to derive equations based on variables passed to it
def newderivative(eq, *args):

    if len(args) == 0:
        eq = diff(eq)
    for sym in args:
        eq = diff(eq, sym)
    return eq


# method to integrate an equation once depending ont the single variable it has
def integration(eq, a=None, b=None):
    if a is None and b is None:
        if 'x' in eq:
            return integrate(eq, x)
        if 'y' in eq:
            return integrate(eq, y)
        if 'z' in eq:
            return integrate(eq, z)
    else:
        if 'x' in eq:
            return integrate(eq, (x, a, b))
        if 'y' in eq:
            return integrate(eq, (y, a, b))
        if 'z' in eq:
            return integrate(eq, (z, a, b))


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
print(newderivative('4*x**2*y**2', x))
print('\nIntegrating testing\n')
# parameters: equation, *symbols
print('indefinite integral ', newintegration('2*x'))
# parameters: equation, *tuple(symbol, lowerbound, upperbound)
print('definite integral ', newintegration('2*x', (x, 0, 2)))

# If the integrand contains more than one free symbol, an integration variable should be supplied explicitly
# parameters: equation, *symbols
print('indefinite integral ', newintegration('2*x**2*y + 2*x*y**2', x, y))
# parameters: equation, *tuple(symbol, lowerbound, upperbound)
print('definite integral ', newintegration('2*x**2*y + 2*x*y**2', (x, 0, 2), (y, 0, 2)))

# variable to be replaced must be initialized as a symbol and sent as a parameter for these methods to work
# parameters: equation, lowerbound, upperbound, symbol
print('\ntesting summation\n')
print(summation('x**2', 0, 6, x))

print('\ntesting product notation\n')
print(productnotation('x**2', 1, 6, x))

print('\ntesting limits\n')
# parameters: equation, x, x0, side to evaluate
print(limits(1/x, x, 0, '+'))
print(limits(sin(x)/x, x, 0))
# testing string replacing for exponent
print('\ntesting formatting\n')
str1 = "4x^2"
print(str1.replace("^", "**"))
print(formateq("4x^2"))
