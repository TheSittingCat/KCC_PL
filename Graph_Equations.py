import matplotlib.pyplot as plt
import math

def point(x, y):
    plt.xlim(x - 5, x + 5)
    plt.ylim(y - 5, y + 5)
    plt.grid()
    plt.plot(x, y, marker = ".")
    return x, y

def line(a = 1, b = 0, rng = (-100, 100)):
    x = [i for i in range(rng[0], rng[1])]
    y = [((a * n) + b) for n in x]
    plt.plot(x, y)
    return y

def x_squared(a = 1, b = 1, c = 0, rng = (-100, 100)):
    x = [i for i in range(rng[0], rng[1])]
    y = [((a * (n ** 2)) + (b * n) + c) for n in x]
    plt.plot(x, y)
    return y

def x_cubed(a = 1, b = 1, c = 1, d = 0, rng = (-100, 100)):
    x = [i for i in range(rng[0], rng[1])]
    y = [((a * (n ** 3)) + (b * (n ** 2)) + (c * n) + d) for n in x]
    plt.plot(x, y)
    return y

def sqrt_x(x = None, rng = (0, 100)):
    if rng[0] < 0:
        raise Exception("Domain error: x values cannot be negative.")
    if x is None:
        x = [i for i in range(rng[0], rng[1])]
    y = [math.sqrt(n) for n in x]
    plt.plot(x, y)
    return y

def abs_val(x = None, rng = (-100, 100)):
    if x is None:
        x = [i for i in range(rng[0], rng[1])]
    y = []
    for n in x:
        if n < 0:
            n = (-1) * n
        y.append(n)
    plt.plot(x, y)
    return y

def exponential(x = None, rng = (-100, 0)):
    e = math.e
    if x is None:
        x = [i for i in range(rng[0], rng[1])]
    y = []
    for n in x:
        y.append(e ** n)
    plt.plot(x, y)
    return y

def log(x = None, base = 10, rng = (1, 100)):
    if x is None:
        x = [i for i in range(rng[0], rng[1])]
    y = []
    for n in x:
        y.append(math.log(n, base))
    plt.plot(x, y)
    return y