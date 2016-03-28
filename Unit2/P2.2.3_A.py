import math

europa_m = 4.8e22 # kg
europa_r = 1560 * 1000# Km - m
g_constant = 6.67259e-11 # m^3*kg^-1*s^-2

europa_mu = g_constant*europa_m

v_esc = math.sqrt(2*europa_mu/europa_r)

v_esc_km = v_esc/1000

print(v_esc_km)
