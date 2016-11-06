from sympy import *

x, y, z, t = symbols('x y z t')


def derivative(eq, d):
    x_value = 0
    y_value = 0
    z_value = 0
    if 'dx' in d:
        x_value = 1
        # print(diff(eq, x))
    if 'dy' in d:
        y_value = 1
        # print(sympy.diff(eq, y))
    if 'dz' in d:
        z_value = 1
        # print(sympy.diff(eq, z))

    return diff(eq, x, x_value, y, y_value, z, z_value)


def integrate(eq, d, xa=None, xb=None, ya=None, yb=None, za=None, zb=None):
    if xa is None and xb is None and ya is None and yb is None and za is None and zb is None:
        if 'dx' in d:
            eq = integrate(eq, x)
        if 'dy' in d:
            eq = integrate(eq, y)
        if 'dz' in d:
            eq = integrate(eq, z)
    else:
        if 'dx' in d:
            eq = integrate(eq, (x, xa, xb))
        if 'dy' in d:
            eq = integrate(eq, (y, ya, yb))
        if 'dz' in d:
            eq = integrate(eq, (z, za, zb))
    return eq


def format_eq(eq):
    if isinstance(eq, str):
        tired = str(eq)
        tired.replace("^", "**")
        return tired


print(derivative('4*x**2*2*y**2', 'dxdy'))
print(diff(4*x**2*2*y**2, x, y))
print(derivative('1/(x**2)', 'dx'))
print(integrate('2*y', 'dy', None, None, 0, 2))
print(integrate('2*x', 'dx', 0, 2))

str1 = "4x^2"
print(str1.replace("^", "**"))
print(format_eq("4x^2"))

