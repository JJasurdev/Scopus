from vpython import *

scene = canvas(title='Charged Particle in Dipole Field')
# Define fixed charges for a dipole at (-1,0,0) and (1,0,0)
charges = [(vector(-1,0,0), +1), (vector(1,0,0), -1)]
for pos, q in charges:
    color = color.red if q > 0 else color.blue
    sphere(pos=pos, radius=0.1, color=color)
# Define a movable test charge
test = sphere(pos=vector(0, -1, 0), radius=0.05, color=color.orange)
q_test = 0.5  # test charge magnitude
velocity = vector(0, 0, 0)
dt = 0.01
# Simulation loop: move the test charge under electrostatic force
for i in range(2000):
    rate(100)
    E = electric_field(test.pos, charges)  # using previously defined function
    F = q_test * E
    # Assume unit mass for simplicity
    velocity += F * dt
    test.pos += velocity * dt
