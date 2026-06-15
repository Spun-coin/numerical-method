import numpy as np

def f(x):
    return 1 / (1 + x * x)

a = 0
b = 6

def trapezoidal(a, b, n):
    h = (b - a) / n
    y = f(np.linspace(a, b, n + 1))
    integral = 0
    for i in range(n):
        integral = integral + (h / 2) * (y[i] + y[i + 1])
    return integral

def simpson13(a, b, n):
    if n % 2 != 0:
        raise Exception("n is not even")
    h = (b - a) / n
    y = f(np.linspace(a, b, n + 1))
    integral = 0
    for i in range(0, n, 2):
        integral = integral + (h / 3) * (y[i] + 4 * y[i + 1] + y[i + 2])
    return integral

def simpson38(a, b, n):
    if n % 3 != 0:
        raise Exception("n is not divisible by 3")
    h = (b - a) / n
    y = f(np.linspace(a, b, n + 1))
    integral = 0
    for i in range(0, n, 3):
        integral = integral + (3 * h / 8) * (y[i] + 3 * y[i + 1] + 3 * y[i + 2] + y[i + 3])
    return integral

def boole(a, b, n):
    if n % 4 != 0:
        raise Exception("n is not divisible by 4")
    h = (b - a) / n
    y = f(np.linspace(a, b, n + 1))
    integral = 0
    for i in range(0, n, 4):
        integral = integral + (2 * h / 45) * (7 * y[i] + 32 * y[i + 1] + 12 * y[i + 2] + 32 * y[i + 3] + 7 * y[i + 4])
    return integral

print("The integral values using different rules:")
print(f"Trapezoidal rule:\t{trapezoidal(a, b, 6):.4f}")
print(f"Simpson's 1/3 rule:\t{simpson13(a, b, 6):.4f}")
print(f"Simpson's 3/8 rule:\t{simpson38(a, b, 6):.4f}")
print(f"Boole's rule:\t\t{boole(a, b, 8):.4f}")