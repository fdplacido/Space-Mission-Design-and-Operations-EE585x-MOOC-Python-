import math

geo_dist = 36000 * 1000  # km - m
earth_r = 6.378e6  # m
earth_mu = 3.986e14

a = 2 * earth_r + 2 * geo_dist
T = 2 * math.pi * math.sqrt(a**3/earth_mu)

print(T/(60*60))

# -----

