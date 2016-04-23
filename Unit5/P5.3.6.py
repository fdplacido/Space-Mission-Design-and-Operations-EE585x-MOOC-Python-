from Constants import constants as const
import math

# Problem A

# v_rotation = rω

earth_ang_rate = 2 * math.pi / const.sideral_day

# v_esc = sqrt(2μ/R + h)

# v_esc = v_rotation

# X = R + h

# sqrt(2μ/X) = ωX

X = math.pow(((2*const.earth_mu)/(earth_ang_rate**2)),(1/3))

h = X - const.earth_r

print("Problem A: " + str(h/1000))  # Km

# Problem B

shadow = 0.4
electric_comp = 500  # W
conversion_eff = 0.25

prod_per_meter = const.solar_constant * (1 - shadow) * conversion_eff

relation = electric_comp/prod_per_meter

print("Problem B: " + str(relation))

# Problem C

alt = 296 * 1000  # Km -> m
tether_long = 20 *1000  # Km -> m
earth_magnetic_field = 3e-5  # T

v_circ = math.sqrt(const.earth_mu/(const.earth_r + alt))

voltage = v_circ*tether_long*earth_magnetic_field

print("Problem C: " + str(voltage/1000))

