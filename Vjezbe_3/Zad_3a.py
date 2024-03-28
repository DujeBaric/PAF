import matplotlib.pyplot as plt
import numpy as np

# Definiranje listi x i y
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Izračunavanje aritmetičke sredine
arth_x = sum(x) / len(x)
arth_y = sum(y) / len(y)

print("Aritmetička sredina za x:", arth_x)
print("Aritmetička sredina za y:", arth_y)

# Izračun standardne devijacije
dev_x = np.sqrt(sum((xi - arth_x)**2 for xi in x) / (len(x) - 1))
dev_y = np.sqrt(sum((yi - arth_y)**2 for yi in y) / (len(y) - 1))

print("Standardna devijacija za x:", dev_x)
print("Standardna devijacija za y:", dev_y)

# Prikaz raspršenog grafikona
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Raspršeni grafikon')
plt.grid(True)
plt.show()
