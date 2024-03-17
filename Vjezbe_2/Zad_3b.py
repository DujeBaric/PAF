import kinematika

sila = 300
masa = 2
vrijeme_koraka = 0.1
ukupno_vrijeme = 10

# Jednoliko gibanje
t1, x1, v1, a1 = kinematika.jednoliko_gibanje(sila, masa, vrijeme_koraka, ukupno_vrijeme)
kinematika.crtaj_grafove(t1, x1, v1, 'jednoliko')

# Kosi hitac
v0 = 25 
theta = 53.13
t2, x2, y2 = kinematika.kosi_hitac(v0, theta, vrijeme_koraka, ukupno_vrijeme)
kinematika.crtaj_grafove(t2, x2, y2, 'kosi_hitac')