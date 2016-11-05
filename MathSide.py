from sympy import *

x, y, z, t = symbols('x y z t')


def derivethis(eq):
    x_value = 0
    y_value = 0
    z_value = 0
    if 'x' in eq:
        x_value = 1
        # print(diff(eq, x))
    if 'y' in eq:
        y_value = 1
        # print(sympy.diff(eq, y))
    if 'z' in eq:
        z_value = 1
        # print(sympy.diff(eq, z))

    return diff(eq, x, x_value, y, y_value, z, z_value)


def integratethis(eq, a = None, b = None):
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




def formatEQ(eq):
    if isinstance(eq, str):
        tired = str(eq)
        tired.replace("^", "**")
        return tired


print(derivethis('4*x**2*2*y**2'))
print(diff(4*x**2*2*y**2, x, y))
print(derivethis('1/(x**2)'))
print(integratethis('2*x'))
print(integratethis('2*x', 0, 2))

str1 = "4x^2"
print(str1.replace("^", "**"))
print(formatEQ("4x^2"))

