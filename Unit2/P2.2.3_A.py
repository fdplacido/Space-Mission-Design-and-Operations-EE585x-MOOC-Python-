from Constants import constants as const
import math

# Problem A

europa_m = 4.8e22  # kg
europa_r = 1560 * 1000  # Km - m

europa_mu = const.g_const*europa_m

v_esc = math.sqrt(2*europa_mu/europa_r)

v_esc_km = v_esc/1000

print("Problem A: " + str(v_esc_km))

# Problem B

jupiter_esc_v = 18.5  # km/s
jupiter_orb_v = 13.1  # km/s

jupiter_trans_v = jupiter_esc_v - jupiter_orb_v

print("Problem B: " + str(jupiter_trans_v))
