import math

sat_dist = 36000 * 1000     # meters
solution_dist = 100 * 1000  # km to m
earth_radius = 6.378e6
grav_const = 6.673e-11
mu_earth = 3.986e14         # GM Earth

# Conservation of mechanical energy
# E_pot1 + E_kin1 = Epot2 + E_kin2
# E_pot = -GMm/r
# E_pot/m = -µ/r
# E_kin = (1/2)mv²
# E_kin/m = (1/2)v²

sat_dist = sat_dist + earth_radius

# E_pot1/m
e_pot_1 = -mu_earth/sat_dist
# E_kin1/m (v=0) is stopped
e_kin_1 = math.pow(0,2)/2
# E_pot2/m
e_pot_2 = -mu_earth/(earth_radius + solution_dist)

# E_pot1/m + E_kin1/m - E_pot2/m = (1/2)v² =>
# √(2 * (E_pot1/m + E_kin1/m - E_pot2/m)) = v

# e_sum = E_pot1/m + E_kin1/m - E_pot2/m
e_sum = e_pot_1 + e_kin_1 - e_pot_2

# √(2 * e_sum)
v_solution = math.sqrt(2*e_sum)

# To km/s
v_solution_km = v_solution / 1000

print(v_solution_km)