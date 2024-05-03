import matplotlib.pyplot as plt
from projectile import Projectile  # Učitavanje klase Projectile iz odvojenog modula

# Parametri projektila
mass = 0.1  # kg
x0 = 0  # m
y0 = 0  # m
velocity = 30  # m/s
density = 1.225  # kg/m^3
area = 0.01  # m^2
drag_coefficient = 0.1
angle = 45  # degrees

# Inicijalizacija projektila
projectile = Projectile(mass, x0, y0, velocity, density, area, drag_coefficient, angle)
time_step = 0.01  # s

# Testiranje s Eulerovom metodom
x_euler, y_euler = projectile.Euler()

# Prikaz rezultata za Eulerovu metodu
plt.figure()
plt.plot(x_euler, y_euler, label="Euler")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Simulacija kosog hitca s otporom zraka koristeći Eulerovu metodu')
plt.grid(True)
plt.legend()

# Testiranje s Runge-Kutta metodom
x_rk, y_rk = projectile.Runge_Kutta()

# Prikaz rezultata za Runge-Kutta metodu
plt.figure()
plt.plot(x_rk, y_rk, label="Runge-Kutta")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Simulacija kosog hitca s otporom zraka koristeći Runge-Kutta metodu')
plt.grid(True)
plt.legend()

plt.show()