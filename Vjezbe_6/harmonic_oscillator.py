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
