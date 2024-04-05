import numpy as np
import matplotlib.pyplot as plt

def linregress(x, y):
    n = len(x)
    xy = np.sum(x * y)
    x_sq = np.sum(x**2)
    x_sum = np.sum(x)
    y_sum = np.sum(y)

    # Izračun nagiba a i presjeka b
    a = (n * xy - x_sum * y_sum) / (n * x_sq - x_sum**2)
    b = (y_sum - a * x_sum) / n

    # Izračun predviđenih vrijednosti
    predicted_y = a * x + b

    return a, b, predicted_y

# Podaci
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])  # Nm
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])  # rad

# Linearna regresija
a, b, predicted_M = linregress(phi, M)

# Grafikon
plt.scatter(phi, M, label='Podaci')
plt.plot(phi, predicted_M, color='red', label='Linearni model')
plt.xlabel('Phi (rad)')
plt.ylabel('M (Nm)')
plt.title('Linearna regresija za modul torzije')
plt.legend()
plt.grid(True)
plt.show()

# Ispis rezultata
print("Nagib a:", a)
print("Presjek b:", b)
