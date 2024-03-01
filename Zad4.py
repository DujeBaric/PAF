def jednadzba_pravca(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2

    if x2 - x1 == 0:
        print("Pravac je vertikalan i nema definiran nagib.")
    else:
        nagib = (y2 - y1) / (x2 - x1)
        print("Jednadžba pravca je y = {}x + {}".format(nagib, y1 - nagib * x1))

# Primjer poziva funkcije:
tocka1 = (1, 2)
tocka2 = (3, 4)
jednadzba_pravca(tocka1, tocka2)