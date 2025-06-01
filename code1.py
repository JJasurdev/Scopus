from vpython import *

# Create a canvas for 3D display
scene = canvas(title='Electric Field of Two Charges')

# Define charges: each is (position, magnitude)
charges = [(vector(-1, 0, 0), +1), (vector(1, 0, 0), -1)]

# Draw the charges as colored spheres
for pos, q in charges:
    color = color.red if q > 0 else color.blue
    sphere(pos=pos, radius=0.1, color=color)

# Function to compute electric field at a point
def electric_field(point, charges):
    E = vector(0, 0, 0)
    for pos, q in charges:
        r = point - pos
        E += q * r / mag(r)**3  # Coulomb's law (k=1 units)
    return E

# Sample points where the field will be drawn (grid on x-y plane)
for x in range(-2, 3):
    for y in range(-2, 3):
        point = vector(x, y, 0)
        E = electric_field(point, charges)
        arrow(pos=point, axis=0.2*E, color=color.yellow)
