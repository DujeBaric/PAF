import matplotlib.pyplot as plt
import numpy as np
import calculus as cls

def f2(x):
    return x**2   # definiram funkciju

# Izračunavanje trapeznih meduja za različite korake
koraci = np.arange(50, 1050, 100)
donje_meduje, gornje_meduje, prosjecne_meduje = [], [], []

for korak in koraci:
    donja, gornja, prosjecna = cls.trapezna(f2, 0, 1, korak)
    donje_meduje.append(donja)
    gornje_meduje.append(gornja)
    prosjecne_meduje.append(prosjecna)

# Crtanje grafa
plt.scatter(koraci, donje_meduje, c="blue", label="Donja granica")
plt.scatter(koraci, gornje_meduje, c="green", label="Gornja granica")
plt.scatter(koraci, prosjecne_meduje, c="red", label="Prosječna vrijednost")
plt.plot(koraci, prosjecne_meduje, c="yellow", label="Prosječna vrijednost (linija)")
plt.legend()
plt.xlabel('Korak')
plt.ylabel('Vrijednost')
plt.title('Trapezna metoda za različite korake')
plt.show()
