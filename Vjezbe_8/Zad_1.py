import numpy as np
import matplotlib.pyplot as plt

# Konstantne
q_electron = -1.602e-19  # Naboj elektrona (Coulombi)
q_positron = 1.602e-19   # Naboj pozitrona (Coulombi)
m = 9.109e-31            # Masa elektrona/pozitrona (kg)
B = np.array([0, 0, 1e-3])  # Magnetno polje [T] (Tesla)

# Početne brzine (m/s)
v0 = np.array([1e6, 1e6, 1e6])

# Početna pozicija (m)
r0 = np.array([0, 0, 0])

# Vrijeme
dt = 1e-11  # Korak integracije (s)
t_max = 1e-7  # Maksimalno vrijeme (s)
t = np.arange(0, t_max, dt)  # Vremenski niz od 0 do t_max s korakom dt

# Funkcija za računanje Lorentzove sile
def lorentz_force(q, v, B):
    return q * np.cross(v, B)  # F = q * (v x B)

# Funkcija za simulaciju gibanja čestice
def simulate_particle(q, v0, r0, t, B):
    r = np.zeros((len(t), 3))  # Inicijalizacija pozicija
    v = np.zeros((len(t), 3))  # Inicijalizacija brzina
    r[0] = r0  # Postavljanje početne pozicije
    v[0] = v0  # Postavljanje početne brzine

    for i in range(1, len(t)):
        F = lorentz_force(q, v[i-1], B)  # Izračun Lorentzove sile
        v[i] = v[i-1] + (F / m) * dt  # Ažuriranje brzine (Eulerova metoda)
        r[i] = r[i-1] + v[i-1] * dt  # Ažuriranje pozicije (Eulerova metoda)

    return r, v  # Vraćanje pozicija i brzina

# Simulacija za elektron
r_electron, v_electron = simulate_particle(q_electron, v0, r0, t, B)

# Simulacija za pozitron
r_positron, v_positron = simulate_particle(q_positron, v0, r0, t, B)

# Plotanje putanja
fig = plt.figure(figsize=(12, 6))  # Kreiranje figure

# Preklopljene putanje elektrona i pozitrona
ax = fig.add_subplot(111, projection='3d')
ax.plot(r_electron[:, 0], r_electron[:, 1], r_electron[:, 2], label='Elektron')  # Plotanje putanje elektrona
ax.plot(r_positron[:, 0], r_positron[:, 1], r_positron[:, 2], color='orange', label='Pozitron')  # Plotanje putanje pozitrona

# Postavljanje naslova i oznaka osi
ax.set_title('Putanja elektrona i pozitrona u magnetnom polju')
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')
ax.legend()  # Prikaz legende

plt.show()  # Prikaz grafa
