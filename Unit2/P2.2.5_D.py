import math

geo_h = 35786 * 1000  # km
earth_mu = 3.986e14  # m^3*s^-2
earth_r = 6.378e6  # m

dist = earth_r + geo_h

v_esc = math.sqrt(2*earth_mu/dist)

v_esc_km = v_esc/1000

print(v_esc_km)
