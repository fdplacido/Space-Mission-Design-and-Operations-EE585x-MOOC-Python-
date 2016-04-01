from Constants import constants as const
import math

# Problem A

# F = (G*M*m)/r^2
# Equal forces
# mu_earth / d_1^2 = mu_sun / d_2^2 ->
# mu_earth / mu_sun = (d_1 / d_2)^2 ->
# sqrt(mu_earth / mu_sun) = d_1/d_2 ->

distances_relation = math.sqrt(const.earth_mu / const.sun_mu)
d_earth = distances_relation*const.astronomical_unit

print("Problem A: " + str(d_earth / 1000))

d_earth_2 = const.astronomical_unit / (1 + (math.sqrt(const.sun_mu /const.earth_mu)))
print("Problem A alt: " + str(d_earth_2 / 1000))

# Problem B

perigee_h = 250 * 1000  # km - m
apogee_h = 800 * 1000  # km - m

semimajor = const.earth_r + ((perigee_h + apogee_h) / 2)
T = 2 * math.pi * math.sqrt((semimajor**3)/ const.earth_mu)

print("Problem B: " + str(T/60))  # secs to min

# Problem D


geo_dist = 36000 * 1000  # km - m

a = 2 * const.earth_r + 2 * geo_dist
T = 2 * math.pi * math.sqrt(a**3/const.earth_mu)

print("Problem D: " + str(T/(60*60)))

