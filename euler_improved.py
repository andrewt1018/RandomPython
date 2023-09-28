import math
def euler_improved(h: float, function, start: tuple, end: float):
    x = start[0]
    y = start[1]
    counter = 0
    while x <= end:
        # Calculate first k
        k0 = function(x, y)
        # Calculate second k
        k1 = function(x + h, y + h * k0)
        y1 = euler_avg(y, h, k0, k1)
        print(f"Iteration {counter}: {round(y1, 4)}")
        counter += 1

        # Update x and y values
        x += h
        y = y1

def euler_avg(y0, h, k0, k1):
    return y0 + (h/2) * (k0 + k1)

def func1(x, y):
    return x + y * y / 2

euler_improved(0.0001, func1, (-2, 0), 2)

def func2(x, y):
    return (-2 * y) + (x ** 3 * math.e ** (-2 * x))



