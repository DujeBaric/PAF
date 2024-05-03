import matplotlib.pyplot as plt
import numpy as np
import projectile as p  # Import klase Projectile iz modula projectile

# Definiranje različitih vremenskih koraka
dts = [0.01, 0.02, 0.05]

# Iteriranje kroz različite vremenske korake
for dt in dts:
    # Inicijalizacija objekta klase Projectile s određenim vremenskim korakom
    projectile = p.Projectile(1, 0, 0, 10, 0.2, 0.2, 0.2, 45, dt)
    
    # Simulacija kretanja projektila koristeći Eulerovu metodu
    x, y = projectile.Euler()
    
    # Prikaži putanju projektila koristeći scatter plot
    plt.scatter(x, y, s=2, label=f'Euler, dt={dt}')

# Inicijalizacija objekta klase Projectile s fiksnim vremenskim korakom (0.01)
projectile = p.Projectile(1, 0, 0, 10, 0.2, 0.2, 0.2, 45, 0.01)

# Simulacija kretanja projektila koristeći Runge-Kutta metodu
x, y = projectile.Runge_Kutta()

# Prikaži putanju projektila koristeći line plot
plt.plot(x, y, label='Runge-Kutta, dt=0.01')

# Prikaz grafikona
plt.xlabel('x')
plt.ylabel('y')
plt.title('Usporedba putanja projektila korištenjem Eulerove i Runge-Kutta metode')
plt.legend()
plt.grid(True)
plt.show()
