import math
from Constants import constants as const

tosend_m = 3  # T

a = (const.astronomical_unit + (const.mars_dist_sun * const.astronomical_unit))/2
v = math.sqrt(((2 * const.sun_mu)/(const.astronomical_unit)) - (const.sun_mu/a))

v_e = math.sqrt(const.sun_mu/const.astronomical_unit)

v_inf = v - v_e

print("Problem A: " + str(v_inf/1000))

# Problem A_2

leave_dist = 500 * 1000 # Km -> m

r_leave = leave_dist + const.astronomical_unit

# v_d^2 = v_inf^2 + v_e^2

v_e_d = math.sqrt((2 * const.earth_mu)/r_leave)

v_d = math.sqrt((v_inf**2) + (v_e_d**2)) - math.sqrt(const.earth_mu/r_leave)

print("Problem A_2: " + str(v_d/1000))

# Problem A_3


