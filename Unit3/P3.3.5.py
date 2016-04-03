import math
from Constants import constants as const

# Problem C

# dΩ/dt = -2.06474e14 (cos(i)/a^3.5(1-e^2)^2)

alt = 350 * 1000  # Km - m
semimajor_axis = alt + const.earth_r
polar_incl = 90

def nodal_regression(angle, semimajaxis, eccentricity):
    return -2.06474e14 * (math.cos(angle)/(semimajaxis**3.5 * (1 - eccentricity**2)**2))

nodal_reg = nodal_regression(polar_incl, semimajor_axis, 0)

print("Problem C: " + str(nodal_reg))

# Problem D
# sun synch orbits

mars_period = 1.88  # years

req_nodal_reg = 360 / (mars_period*const.full_year)

print("Problem D: " + str(req_nodal_reg))

# Problem F

