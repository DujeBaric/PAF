import numpy as np

def main():
    # Definiranje lista x i y
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Izračunavanje aritmetičke sredine
    aritmeticka_sredina_x = np.mean(x)
    aritmeticka_sredina_y = np.mean(y)

    # Izračunavanje standardne devijacije
    standardna_devijacija_x = np.std(x)
    standardna_devijacija_y = np.std(y)

    # Ispis rezultata
    print("Aritmetička sredina za x:", aritmeticka_sredina_x)
    print("Aritmetička sredina za y:", aritmeticka_sredina_y)
    print("Standardna devijacija za x:", standardna_devijacija_x)
    print("Standardna devijacija za y:", standardna_devijacija_y)

if __name__ == "__main__":
    main()
