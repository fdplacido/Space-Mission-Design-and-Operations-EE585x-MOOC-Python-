import math

perigee_h = 250 * 1000  # km - m
apogee_h = 800 * 1000  # km - m
earth_r = 6.378e6  # m
mu_earth = 3.986e14  # m^3 / s^2

semimajor = earth_r + ((perigee_h + apogee_h) / 2)
T = 2 * math.pi * math.sqrt((semimajor**3)/ mu_earth)

print(T/60)  # secs to min