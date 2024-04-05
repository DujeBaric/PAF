import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v, kut, x0, y0, dt=0.1):
        self.v = v
        self.kut = math.radians(kut)
        self.x0 = x0
        self.y0 = y0
        self.dt = dt
        self.g = 9.81
        self.reset()

    def reset(self):
        self.vx0 = self.v * math.cos(self.kut)
        self.vy0 = self.v * math.sin(self.kut)
        self.x = [self.x0]
        self.y = [self.y0]
        self.vx = [self.vx0]
        self.vy = [self.vy0]
        self.t = [0]

    def __move(self):
        self.x.append(self.x[-1] + self.vx[-1] * self.dt)
        self.y.append(self.y[-1] + self.vy[-1] * self.dt)
        self.vx.append(self.vx[-1] - self.dt * 0)  # Ovdje bi trebao biti faktor otpora zraka ili slično
        self.vy.append(self.vy[-1] - self.dt * self.g)
        self.t.append(self.t[-1] + self.dt)

    def range(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1]

    def plot_trajectory(self):
        self.reset()
        while self.y[-1] >= 0:
            self.__move()
        plt.plot(self.x, self.y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Trajectory of the Particle')
        plt.grid(True)
        plt.show()

    def analiticki_domet(self):
        return (self.v ** 2 * math.sin(2 * self.kut)) / self.g
