from sympy import *
# ALL VARIABLES USED IN EQUATIONS MUST BE DECLARED AS SYMBOLS OR ELSE SYMPY METHODS WILL NOT RECOGNIZE THEM
x, y, z, t, a = symbols('x y z t a')


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
def formatEQ(eq):
    if isinstance(eq, str):
        tired = str(eq)
        tired.replace("^", "**")
        return tired

print("derivations testing\n")
print(newderivative('1/(a**2)'))
# If there's more than one variable in the exp, the variable(s) of differentiation must be supplied to differentiate
print(newderivative('4*x**2*y**2', x))
print('Integrating testing\n')
print('indefinite integral ', newintegration('2*x'))
print('definite integral ', newintegration('2*x', (x, 0, 2)))

# If the integrand contains more than one free symbol, an integration variable should be supplied explicitly
print('indefinite integral ', newintegration('2*x**2*y + 2*x*y**2', x, y))
print('definite integral ', newintegration('2*x**2*y + 2*x*y**2', (x, 0, 2), (y, 0, 2)))


# testing string replacing for exponent
str1 = "4x^2"
print(str1.replace("^", "**"))
print(formatEQ("4x^2"))

