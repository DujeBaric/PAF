import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(sila, masa, vrijeme_koraka, ukupno_vrijeme):
    a = sila / masa

    x, v = 0.0, 0.0
    lista_t, lista_x, lista_v, lista_a = [], [], [], []

    for t in np.arange(0, ukupno_vrijeme + vrijeme_koraka, vrijeme_koraka):
        x += v * vrijeme_koraka
        v += a * vrijeme_koraka

        lista_t.append(t)
        lista_x.append(x)
        lista_v.append(v)
        lista_a.append(a)

    return lista_t, lista_x, lista_v, lista_a

def kosi_hitac(v0, theta, vrijeme_koraka, ukupno_vrijeme):
    g = 9.81
    theta_rad = np.radians(theta)

    x, y, vx, vy = 0.0, 0.0, v0 * np.cos(theta_rad), v0 * np.sin(theta_rad)
    lista_t, lista_x, lista_y = [], [], []

    for t in np.arange(0, ukupno_vrijeme + vrijeme_koraka, vrijeme_koraka):
        ax, ay = 0.0, -g

        vx += ax * vrijeme_koraka
        vy += ay * vrijeme_koraka

        x += vx * vrijeme_koraka
        y += vy * vrijeme_koraka

        lista_t.append(t)
        lista_x.append(x)
        lista_y.append(y)

    return lista_t, lista_x, lista_y

def crtaj_grafove(lista_t, lista_x, lista_y, tip):
    if tip == 'jednoliko':
        plt.plot(lista_t, lista_x, label='x-t Graf')
        plt.plot(lista_t, lista_y, label='v-t Graf')
    elif tip == 'kosi_hitac':
        plt.plot(lista_x, lista_y, label='x-y Graf')

    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj (m) / Brzina (m/s)')
    plt.legend()
    plt.grid(True)
    plt.show()