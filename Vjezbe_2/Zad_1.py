import matplotlib.pyplot as plt

def jednoliko_gibanje(sila, masa, vrijeme_koraka, ukupno_vrijeme):
    x, v, a = 0.0, 0.0, sila / masa

    lista_t, lista_x, lista_v, lista_a = [], [], [], []

    for t in range(0, ukupno_vrijeme + vrijeme_koraka, vrijeme_koraka):
        x += v * vrijeme_koraka
        v += a * vrijeme_koraka

        lista_t.append(t)
        lista_x.append(x)
        lista_v.append(v)
        lista_a.append(a)

    return lista_t, lista_x, lista_v, lista_a

def crtaj_grafove(lista_t, lista_x, lista_v, lista_a):
    plt.plot(lista_t, lista_x, label='x-t Graf')
    plt.plot(lista_t, lista_v, label='v-t Graf')
    plt.plot(lista_t, lista_a, label='a-t Graf')

    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Pozicija (m), Brzina (m/s), Ubrzanje (m/s^2)')
    plt.legend()
    plt.grid(True)
    plt.show()

sila = 100
masa = 1
vrijeme_koraka = 1
ukupno_vrijeme = 5

t, x, v, a = jednoliko_gibanje(sila, masa, vrijeme_koraka, ukupno_vrijeme)
crtaj_grafove(t, x, v, a)