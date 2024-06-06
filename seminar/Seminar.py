import matplotlib.pyplot as plt
import numpy as np

def provjeri_tocku(x_tocka, y_tocka, x_centar, y_centar, radijus, ime_datoteke=None):
    # Izračunaj udaljenost točke od centra kružnice
    udaljenost = np.sqrt((x_tocka - x_centar) ** 2 + (y_tocka - y_centar) ** 2)
    
    # Provjeri položaj točke
    if radijus == 0:
        if x_tocka == x_centar and y_tocka == y_centar:
            pozicija = "točno na (središtu)"
        else:
            pozicija = "izvan"
        print(f"Kružnica je točka s radijusom 0.")
    else:
        if udaljenost < radijus:
            pozicija = "unutar"
        elif udaljenost == radijus:
            pozicija = "točno na"
        else:
            pozicija = "izvan"
    
    # Ispiši položaj i udaljenost
    print(f"Točka je {pozicija} kružnice.")
    print(f"Udaljenost od kružnice: {udaljenost:.2f}")
    
    # Crtaj kružnicu i točku
    fig, ax = plt.subplots()
    if radijus != 0:
        kruznica = plt.Circle((x_centar, y_centar), radijus, fill=False, color='blue')
        ax.add_artist(kruznica)
    
    plt.plot(x_tocka, y_tocka, 'ro')  # crvena točka
    plt.plot(x_centar, y_centar, 'bo', markersize=5)  # plava točka za središte
    
    # Postavljanje granica grafa
    max_dist = max(radijus, udaljenost) + 1
    ax.set_xlim(x_centar - max_dist, x_centar + max_dist)
    ax.set_ylim(y_centar - max_dist, y_centar + max_dist)
    ax.set_aspect('equal', 'box')
    plt.grid(True)

    # Dodajanje oznaka
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Dodaj naslov
    ax.set_title(f"Točka je {pozicija} kružnice")

    # Prikaz slike
    plt.show()
    
    # Spremanje slike ako je ime datoteke zadano
    if ime_datoteke:
        fig.savefig(ime_datoteke)
        print(f"Slika je spremljena kao {ime_datoteke}")

def main():
    x_tocka = float(input("Unesite x koordinatu točke: "))
    y_tocka = float(input("Unesite y koordinatu točke: "))
    x_centar = float(input("Unesite x koordinatu središta kružnice: "))
    y_centar = float(input("Unesite y koordinatu središta kružnice: "))
    radijus = float(input("Unesite radijus kružnice: "))
    
    spremi = input("Želite li spremiti sliku? (da/ne): ").strip().lower() == 'da'
    ime_datoteke = None
    if spremi:
        ime_datoteke = input("Unesite ime datoteke za spremanje slike (s ekstenzijom, npr. 'slika.png'): ").strip()
    
    provjeri_tocku(x_tocka, y_tocka, x_centar, y_centar, radijus, ime_datoteke)

if __name__ == "__main__":
    main()