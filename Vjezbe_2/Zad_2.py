import matplotlib.pyplot as plt
import numpy as np

# Funkcija za izračun gibanja projektila
def gibanje_projektila(v0, theta, vrijeme_koraka, ukupno_vrijeme):
    g = 9.81
    theta_rad = np.radians(theta)

    # Početni uvjeti: položaj (x, y) i brzina (vx, vy)
    x, y, vx, vy = 0.0, 0.0, v0 * np.cos(theta_rad), v0 * np.sin(theta_rad)
    
    # Liste za pohranu vremena, položaja po x i položaja po y
    lista_t, lista_x, lista_y = [], [], []

    # Petlja koja simulira gibanje projektila
    for t in np.arange(0, ukupno_vrijeme + vrijeme_koraka, vrijeme_koraka):
        # Ubacivanje ubrzanja (ax, ay)
        ax, ay = 0.0, -g

        # Ažuriranje brzina koristeći ubrzanje
        vx += ax * vrijeme_koraka
        vy += ay * vrijeme_koraka

        # Ažuriranje položaja koristeći brzine
        x += vx * vrijeme_koraka
        y += vy * vrijeme_koraka

        # Dodavanje trenutnog vremena i položaja u liste
        lista_t.append(t)
        lista_x.append(x)
        lista_y.append(y)

    return lista_t, lista_x, lista_y

# Funkcija za crtanje grafova
def crtaj_grafove(lista_t, lista_x, lista_y):
    # Graf položaja y u ovisnosti o položaju x
    plt.plot(lista_x, lista_y, label='x-y Graf')
    plt.xlabel('Položaj x (m)')
    plt.ylabel('Položaj y (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Graf položaja x u ovisnosti o vremenu
    plt.plot(lista_t, lista_x, label='x-t Graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj x (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Graf položaja y u ovisnosti o vremenu
    plt.plot(lista_t, lista_y, label='y-t Graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj y (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Početni uvjeti i parametri simulacije
v0 = 10
theta = 45
vrijeme_koraka = 0.1
ukupno_vrijeme = 10

# Poziv funkcije za izračun gibanja projektila
t, x, y = gibanje_projektila(v0, theta, vrijeme_koraka, ukupno_vrijeme)

# Poziv funkcije za crtanje grafova
crtaj_grafove(t, x, y)