import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation  
from planeti import simulate_bodies 

# Konstante
AU = 1.496e11  # Astronomska jedinica (m)
year_in_seconds = 365.242 * 24 * 3600  # Jedna godina u sekundama

# Početni uvjeti za Sunce i Zemlju
bodies = {
    'Sun': {
        'mass': 1.989e30,  # Masa Sunca u kilogramima
        'position': np.array([0.0, 0.0]),  # Početna pozicija Sunca (x, y)
        'velocity': np.array([0.0, 0.0])  # Početna brzina Sunca (vx, vy)
    },
    'Earth': {
        'mass': 5.9742e24,  # Masa Zemlje u kilogramima
        'position': np.array([AU, 0.0]),  # Početna pozicija Zemlje (x, y)
        'velocity': np.array([0.0, 29783.0])  # Početna brzina Zemlje (vx, vy)
    }
}

# Vremenski parametri
dt = 60 * 60  # Korak integracije (jedan sat)
t_max = year_in_seconds  # Simulacija jedne godine
steps = int(t_max / dt)  # Broj koraka simulacije

# Simulacija
positions = simulate_bodies(bodies, dt, steps)  # Pozivanje funkcije simulate_bodies za simulaciju gibanja tijela

# Inicijalizacija putanja
earth_path = np.zeros((steps, 2))  # Inicijalizacija niza za pohranu putanje Zemlje
sun_path = np.zeros((steps, 2))  # Inicijalizacija niza za pohranu putanje Sunca

# Animacija
fig, ax = plt.subplots()  # Inicijalizacija figure i osi za crtanje
ax.set_xlim(-2*AU, 2*AU)  # Postavljanje granica osi x
ax.set_ylim(-2*AU, 2*AU)  # Postavljanje granica osi y
line_sun, = ax.plot([], [], 'yo', markersize=10, label='Sun')  # Inicijalizacija crteža Sunca
line_earth, = ax.plot([], [], 'bo', markersize=5, label='Earth')  # Inicijalizacija crteža Zemlje
line_earth_path, = ax.plot([], [], 'b--', label='Earth Path')  # Inicijalizacija crteža putanje Zemlje kao linije
line_sun_path, = ax.plot([], [], 'y--', label='Sun Path')  # Inicijalizacija crteža putanje Sunca kao linije

def init():
    line_sun.set_data([], [])  # Postavljanje početnih podataka za Sunce
    line_earth.set_data([], [])  # Postavljanje početnih podataka za Zemlju
    line_earth_path.set_data([], [])  # Postavljanje početnih podataka za putanju Zemlje
    line_sun_path.set_data([], [])  # Postavljanje početnih podataka za putanju Sunca
    return line_sun, line_earth, line_earth_path, line_sun_path  # Vraćanje crteža

def update(frame):
    line_sun.set_data(positions['Sun'][frame, 0], positions['Sun'][frame, 1])  # Ažuriranje pozicije Sunca
    line_earth.set_data(positions['Earth'][frame, 0], positions['Earth'][frame, 1])  # Ažuriranje pozicije Zemlje
    
    # Ažuriranje putanja
    earth_path[frame] = positions['Earth'][frame]  # Pohrana nove pozicije Zemlje
    sun_path[frame] = positions['Sun'][frame]  # Pohrana nove pozicije Sunca
    line_earth_path.set_data(earth_path[:frame+1, 0], earth_path[:frame+1, 1])  # Ažuriranje putanje Zemlje kao linije
    line_sun_path.set_data(sun_path[:frame+1, 0], sun_path[:frame+1, 1])  # Ažuriranje putanje Sunca kao linije
    
    return line_sun, line_earth, line_earth_path, line_sun_path  # Vraćanje crteža

ani = animation.FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, interval=1)  # Stvaranje animacije

plt.legend()  # Dodavanje legende na grafikon
plt.title('Putanja Sunca i Zemlje')  # Postavljanje naslova grafikona
plt.xlabel('X [m]')  # Postavljanje oznake x osi
plt.ylabel('Y [m]')  # Postavljanje oznake y osi
plt.grid(True)  # Uključivanje mreže na grafikonu
plt.show()  # Prikaz grafikona i animacije
