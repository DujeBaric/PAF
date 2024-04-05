import numpy as np
import matplotlib.pyplot as plt
import particle as part

v0 = 10
kut = 60
x0 = 0
y0 = 0

t = 0.001
vrijeme = []
error = []

while t <= 0.1:
    p = part.Particle(v0, kut, x0, y0, t)
    err = (np.abs(p.range() - p.analiticki_domet()) / p.analiticki_domet()) * 100
    error.append(err)
    vrijeme.append(t)
    t += 0.001

plt.plot(vrijeme, error)
plt.xlabel('Vremenski korak (dt)')
plt.ylabel('Relativna pogreška (%)')
plt.title('Relativna pogreška u ovisnosti o vremenskom koraku')
plt.grid(True)
plt.show()
