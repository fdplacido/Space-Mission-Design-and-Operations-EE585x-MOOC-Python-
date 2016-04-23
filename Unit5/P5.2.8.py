from Constants import constants as const
import math

diameter = 3.6  # m
I = 500  # Kg m^2
Thrust_f = 3.5  # N
Isp = 190  # s
angle = 90  # deg
angle_rad = math.pi

# θ = (nFL/I_v)t^2 + (nFL/I_v)t x t_c
# t_c = 0
# θ = (nFL/I_v) * t^2
# t^2 = (θ * I_v) / nFL

t_square = (angle_rad * I) / (2 * 2 * Thrust_f * (diameter/2))
t = math.sqrt(t_square)

print("Problem D: " + str(2*t))

# prop used
# m_p = 2 * t_b * mp_p
# m_p = (2n F * t_b) / (g * Isp)

earth_g = const.earth_mu / (const.earth_r**2)

m_p = (2 * 2 * Thrust_f * t) / (earth_g * Isp)

print("Problem D_2: " + str(m_p*1000))  # Kg -> g
