import matplotlib.pyplot as plt
import math

def line(a = 1, b = 0, rng = (-100, 100)):
    x = [i for i in range(rng[0], rng[1])]
    y = [((a * n) + b) for n in x]
    plt.plot(x, y)
    plt.show()
    return y

y1 = line(-4, 5)
y2 = line(2)

def x_squared(a = 1, b = 1, c = 0, rng = (-100, 100)):
    x = [i for i in range(rng[0], rng[1])]
    y = [((a * (n ** 2)) + (b * n) + c) for n in x]
    plt.plot(x, y)
    plt.show()
    return y

y3 = x_squared(1, 2, 3)

def x_cubed(a = 1, b = 1, c = 1, d = 0, rng = (-100, 100)):
    x = [i for i in range(rng[0], rng[1])]
    y = [((a * (n ** 3)) + (b * (n ** 2)) + (c * n) + d) for n in x]
    plt.plot(x, y)
    plt.show()
    return y

y4 = x_cubed(1, 2, 3, 4)

def sqrt_x(x = None, rng = (0, 100)):
    if rng[0] < 0:
        raise Exception("Domain error: x values cannot be negative.")
    if x is None:
        x = [i for i in range(rng[0], rng[1])]
    y = [math.sqrt(n) for n in x]
    plt.plot(x, y)
    plt.show()
    return y

y5 = sqrt_x()

def abs_val(x = None, rng = (-100, 100)):
    if x is None:
        x = [i for i in range(rng[0], rng[1])]
    y = []
    for n in x:
        if n < 0:
            n = (-1) * n
        y.append(n)
    plt.plot(x, y)
    plt.show()
    return y

y6 = abs_val()
y7 = abs_val(y2)
y8 = sqrt_x(y7)

