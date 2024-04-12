import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**3

def derivacija(f, x, h):
    return (f(x + h) - f(x)) / h

def der(f, a, b, h):
    x_values = np.arange(a, b, h)
    y_values = [derivacija(f, x, h) for x in x_values]
    return x_values, y_values

a, b = der(f1, -2, 2, 0.1)
c, d = der(f1, -2, 2, 0.01)

plt.scatter(a, b, s=2, c="red")
plt.plot(c, d)
plt.show()
