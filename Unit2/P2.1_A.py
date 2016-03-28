iss_orbit_apogee = 417 * 1000 # Km to m
iss_orbit_perigee = 401 * 1000 # Km to m
earth_mu = 3.986e14 # m^3/s^-2
earth_r = 6.378e6 # m

dist = earth_r + iss_orbit_perigee
grav = earth_mu / dist**2

print(grav)