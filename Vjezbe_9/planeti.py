import numpy as np

G = 6.67408e-11  # Gravitacijska konstanta (Nm^2/kg^2)

def calculate_gravitational_force(m1, m2, r1, r2):
    r = r2 - r1
    distance = np.linalg.norm(r)
    if distance == 0:
        return np.array([0.0, 0.0])
    force_magnitude = G * m1 * m2 / distance**2
    force_direction = r / distance
    return force_magnitude * force_direction

def simulate_bodies(bodies, dt, steps):
    positions = {name: np.zeros((steps, 2)) for name in bodies.keys()}
    
    for i in range(steps):
        forces = {name: np.array([0.0, 0.0]) for name in bodies.keys()}
        
        for name1, body1 in bodies.items():
            for name2, body2 in bodies.items():
                if name1 != name2:
                    forces[name1] += calculate_gravitational_force(body1['mass'], body2['mass'], body1['position'], body2['position'])
        
        for name, body in bodies.items():
            acceleration = forces[name] / body['mass']
            body['velocity'] += acceleration * dt
            body['position'] += body['velocity'] * dt
            positions[name][i] = body['position']
    
    return positions
