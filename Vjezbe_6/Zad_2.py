import numpy as np

class HarmonicOscillator:
    def __init__(self, mass, spring_constant, initial_position, initial_velocity):
        self.mass = mass
        self.spring_constant = spring_constant
        self.position = initial_position
        self.velocity = initial_velocity
    
    def update(self, dt):
        acceleration = -self.spring_constant * self.position / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
    
    def simulate(self, total_time, dt):
        num_steps = int(total_time / dt)
        positions = np.zeros(num_steps)
        velocities = np.zeros(num_steps)
        accelerations = np.zeros(num_steps)
        times = np.linspace(0, total_time, num_steps)

        for i in range(num_steps):
            positions[i] = self.position
            velocities[i] = self.velocity
            accelerations[i] = -self.spring_constant * self.position / self.mass
            self.update(dt)
        
        return times, positions, velocities, accelerations
    
    def calculate_period(self, tolerance=1e-6, max_iterations=1000):
        # Postavljamo početne uvjete
        t = 0
        initial_position = self.position
        sign_change_count = 0
        sign = np.sign(initial_position)
        
        # Računamo period titranja
        while sign_change_count < 2 and t < max_iterations:
            self.update(dt=0.01)  # Koristimo manji korak za veću preciznost
            if np.sign(self.position) != sign:
                sign = np.sign(self.position)
                sign_change_count += 1
            t += 1
        
        if t >= max_iterations:
            return None  # Nije pronađen period unutar maksimalnog broja iteracija
        
        return t * 0.01  # Period je jednak broju koraka pomnoženom s korakom vremena

# Primjer upotrebe
mass = 1.0
spring_constant = 1.0
initial_position = 1.0
initial_velocity = 0.0

oscillator = HarmonicOscillator(mass, spring_constant, initial_position, initial_velocity)
period = oscillator.calculate_period()
print("Numerički izračunati period titranja:", period)
