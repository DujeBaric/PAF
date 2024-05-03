import numpy as np

class Projectile:
    def __init__(self, mass, x0, y0, velocity, density, area, drag_coefficient, angle, dt=0.01):
        """
        Konstruktor klase Projectile.
        
        Args:
            mass (float): Masa projektila u kg.
            x0 (float): Početna x-koordinata projektila u m.
            y0 (float): Početna y-koordinata projektila u m.
            velocity (float): Početna brzina projektila u m/s.
            density (float): Gustoća zraka u kg/m^3.
            area (float): Poprečna površina projektila izložena zraku u m^2.
            drag_coefficient (float): Koeficijent otpora zraka.
            angle (float): Početni kut otklona projektila u stupnjevima.
            dt (float, opcionalno): Vremenski korak za simulaciju u s. 
                Zadano je 0.01 s.
        """
        self.mass = mass
        self.x0 = x0
        self.y0 = y0
        self.velocity = velocity
        self.density = density
        self.area = area
        self.drag_coefficient = drag_coefficient
        self.angle = angle
        self.dt = dt
        self.x = []  # Lista za pohranu x-koordinata tijekom simulacije.
        self.y = []  # Lista za pohranu y-koordinata tijekom simulacije.

    def Euler(self):
        """
        Metoda za simulaciju kretanja projektila koristeći Eulerovu metodu.

        Returns:
            x (list): Lista x-koordinata tijekom simulacije.
            y (list): Lista y-koordinata tijekom simulacije.
        """
        t = 0  # Inicijalno vrijeme
        g = 9.81  # Gravitacijsko ubrzanje u m/s^2

        # Početne x i y komponente brzine
        vx = self.velocity * np.cos(np.radians(self.angle))
        vy = self.velocity * np.sin(np.radians(self.angle))

        # Glavna petlja simulacije dok je y-koordinata veća ili jednaka nuli
        while self.y0 >= 0:
            # Računanje ubrzanja koristeći Eulerovu metodu
            ax = -np.sign(vx) * ((self.density * self.drag_coefficient * self.area) / (2 * self.mass)) * (vx ** 2)
            ay = -g - np.sign(vy) * ((self.density * self.drag_coefficient * self.area) / (2 * self.mass)) * (vy ** 2)
            # Ažuriranje brzine i položaja koristeći Eulerovu metodu
            vx += ax * self.dt
            vy += ay * self.dt
            self.x0 += vx * self.dt
            self.y0 += vy * self.dt

            # Pohrana trenutnih položaja u liste
            self.x.append(self.x0)
            self.y.append(self.y0)
            t += self.dt  # Ažuriranje vremena

        return self.x, self.y

    def Runge_Kutta(self):
        """
        Metoda za simulaciju kretanja projektila koristeći Runge-Kutta metodu.

        Returns:
            x (list): Lista x-koordinata tijekom simulacije.
            y (list): Lista y-koordinata tijekom simulacije.
        """
        t = 0  # Inicijalno vrijeme
        g = 9.81  # Gravitacijsko ubrzanje u m/s^2

        # Početne x i y komponente brzine
        vx = self.velocity * np.cos(np.radians(self.angle))
        vy = self.velocity * np.sin(np.radians(self.angle))

        # Glavna petlja simulacije dok je y-koordinata veća ili jednaka nuli
        while self.y0 >= 0:
            # Računanje ubrzanja koristeći Runge-Kutta metodu
            s = (self.density * self.drag_coefficient * self.area) / (2 * self.mass)
            k1vx = (-np.sign(vx) * s * vx ** 2) * self.dt
            k1vy = (g - np.sign(vy) * s * vy ** 2) * self.dt
            k2vx = (-np.sign(vx + (k1vx / 2)) * s * (vx + (k1vx / 2)) ** 2) * self.dt
            k2vy = (g - np.sign(vy + (k1vy / 2)) * s * (vy + (k1vy / 2)) ** 2) * self.dt
            k3vx = (-np.sign(vx + (k2vx / 2)) * s * (vx + (k2vx / 2)) ** 2) * self.dt
            k3vy = (g - np.sign(vy + (k2vy / 2)) * s * (vy + (k2vy / 2)) ** 2) * self.dt
            k4vx = (-np.sign(vx + k3vx) * s * (vx + k3vx) ** 2) * self.dt
            k4vy = (g - np.sign(vy + k3vy) * s * (vy + k3vy) ** 2) * self.dt
            # Ažuriranje brzine i položaja koristeći Runge-Kutta metodu
            vx += (1 / 6) * (k1vx + 2 * k2vx + 2 * k3vx + k4vx)
            vy += (1 / 6) * (k1vy + 2 * k2vy + 2 * k3vy + k4vy)
            self.x0 += vx * self.dt
            self.y0 += vy * self.dt

            # Pohrana trenutnih položaja u liste
            self.x.append(self.x0)
            self.y.append(self.y0)
            t += self.dt  # Ažuriranje vremena

        return self.x, self.y
