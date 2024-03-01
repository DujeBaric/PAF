import matplotlib.pyplot as plt

def jednadzba_pravca(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2

    if x2 - x1 == 0:
        print("Pravac je vertikalan i nema definiran nagib.")
        return None, None
    else:
        nagib = (y2 - y1) / (x2 - x1)
        pomak = y1 - nagib * x1
        return nagib, pomak

def nacrtaj_graf(tocka1, tocka2, nagib, pomak, prikazi=True, ime_pdf=None):
    x1, y1 = tocka1
    x2, y2 = tocka2
    x_values = [x1, x2]
    y_values = [y1, y2]

    plt.scatter(x_values, y_values, color='red', label='Točke')

    if nagib is not None and pomak is not None:
        x_range = [min(x_values), max(x_values)]
        y_range = [nagib*x + pomak for x in x_range]
        plt.plot(x_range, y_range, linestyle='--', color='blue', label='Pravac')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graf pravca kroz dvije točke')
    plt.legend()

    if prikazi:
        plt.show()
    elif ime_pdf:
        plt.savefig(ime_pdf + '.pdf')

# Primjer poziva funkcije:
tocka1 = (1, 2)
tocka2 = (3, 4)
nagib, pomak = jednadzba_pravca(tocka1, tocka2)
nacrtaj_graf(tocka1, tocka2, nagib, pomak, prikazi=True)