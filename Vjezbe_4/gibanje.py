import particle as part

p1 = part.Particle(5, 45, 0, 0)
print("Numerički domet:", p1.range())
print("Analitički domet:", p1.analiticki_domet())

p1.plot_trajectory()
