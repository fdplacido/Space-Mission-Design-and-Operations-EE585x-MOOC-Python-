import math
from Constants import constants as const

shuttle_alt = 296  # Km
tether_long = 20  # Km
shuttle_m = 100 * 1000  # t -> Kg
sat_m = 500  # Kg
cable_alt = 315.9  # Km

# From problem in Unit 5

d_ss = 100  # m
d_sat = 19.9 * 1000 # Km -> m
h_ss = 295.9 * 1000  # km -> m
h_sat = 315.9 * 1000  # Km -> m

r_c = const.earth_r + shuttle_alt
r_sat = r_c + d_sat
r_ss = r_c - d_ss

# Orbital velocity

v_c = math.sqrt(const.earth_mu/r_c)

v_tan = v_c * r_sat/r_c

v_circ = math.sqrt(const.earth_mu/r_sat)

delta_v = v_tan - v_circ

# d = 3.5 v (for LEO)

r_a = 3.5 * delta_v

a = 1/2 * 3.5 * delta_v

print("Problem B: " + str(a))

