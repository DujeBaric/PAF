def unos_koordinata():
    while True:
        try:
            x = float(input("Unesite x koordinatu: "))
            y = float(input("Unesite y koordinatu: "))
            return x, y
        except ValueError:
            print("Pogrešan unos. Molimo ponovite.")

def jednadzba_pravca(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2
    if x1 == x2:
        return "x = ", x1
    else:
        k = (y2 - y1) / (x2 - x1)
        n = y1 - k * x1
        return "y = ", k, "x + ", n

def main():
    print("Unesite koordinate prve točke:")
    tocka1 = unos_koordinata()
    print("Unesite koordinate druge točke:")
    tocka2 = unos_koordinata()

    jednadzba = jednadzba_pravca(tocka1, tocka2)
    print("Jednadzba pravca koji prolazi kroz te dvije točke je:")
    for elem in jednadzba:
        print(elem, end=" ")

if __name__ == "__main__":
    main()