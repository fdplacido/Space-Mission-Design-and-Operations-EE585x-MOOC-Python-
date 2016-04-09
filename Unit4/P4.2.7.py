from Constants import constants as const
import math

# Problem A

spacecraft_alt = 1000 * 1000  # Km - m
departure_v = 11 * 1000  # km/s - m/s

spacecraft_orbit = spacecraft_alt + const.earth_r

# conservation of energy
# v_S^2 / 2 - μ / r_S = v_d^2 / 2 - μ / r_d

# sphere of influence
# r_S = R(μ/μ)^(2/5)

r_S = const.astronomical_unit * (const.earth_mu/const.sun_mu)**(2/5)

conservation_left_side = (departure_v**2)/2 - (const.earth_mu/spacecraft_orbit)

v_S = math.sqrt(2 * (conservation_left_side + (const.earth_mu/r_S)))

print("Problem A: " + str(v_S/1000))

# Problem B

# Half the period
# T = 2π sqrt(a^3/mu)

a = (1 + const.mars_dist_sun)/2
a *= const.astronomical_unit
T = 2 * math.pi * math.sqrt((a**3)/const.sun_mu)
T /= 2

print("Problem B: " + str(T/(60*60*24)))  # to days


