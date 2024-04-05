def calculate_result(N):
    result = 0
    for i in range(N):
        result += 1/3
    for i in range(N):
        result -= 1/3
    result += 5  # Dodajemo 5 na konačni rezultat
    return result

# Ispis rezultata za 200, 2000 i 20000 iteracija s više decimalnih mjesta
print("Rezultat za 200 iteracija:", "{:.20f}".format(calculate_result(200)))
print("Rezultat za 2000 iteracija:", "{:.20f}".format(calculate_result(2000)))
print("Rezultat za 20000 iteracija:", "{:.20f}".format(calculate_result(20000)))
#Iako želimo rezultat blizu broja 5, akumulirana pogreška u računanju dovodi do rezultata koji je vrlo blizu 5, ali nije točno 5.
