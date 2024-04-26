import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator

# Parametri oscilatora
mass = 1.0
spring_constant = 1.0
initial_position = 1.0
initial_velocity = 0.0
total_time = 10.0
dt_values = [0.1, 0.01, 0.001]  # Različiti koraci vremena

# Simulacija i crtanje grafova za svaki dt
for dt in dt_values:
    oscillator = HarmonicOscillator(mass, spring_constant, initial_position, initial_velocity)
    times, positions, velocities, accelerations = oscillator.simulate(total_time, dt)
    
    # x - t graf
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.plot(times, positions)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title(f'Position vs Time (dt = {dt})')

    # v - t graf
    plt.subplot(1, 3, 2)
    plt.plot(times, velocities)
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title(f'Velocity vs Time (dt = {dt})')

    # a - t graf
    plt.subplot(1, 3, 3)
    plt.plot(times, accelerations)
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.title(f'Acceleration vs Time (dt = {dt})')

    plt.tight_layout()
    plt.show()
