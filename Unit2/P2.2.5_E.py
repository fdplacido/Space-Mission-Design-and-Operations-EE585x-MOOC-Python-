import math

pluto_m = 1.3e22  # kg
pluto_r = 1200 * 1000  # km
g_constant = 6.67259e-11  # m^3*kg^-1*s^-2

esc_v = math.sqrt(2*g_constant*pluto_m/pluto_r)

esc_v_km = esc_v/1000

print(esc_v_km)
