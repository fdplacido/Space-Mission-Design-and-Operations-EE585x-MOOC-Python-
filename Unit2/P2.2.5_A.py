from Constants import constants as const
import math

deimos_m = 1.48e15  # kg
deimos_r = 6.2 * 1000  # km - m

deimos_g = const.g_const * deimos_m / deimos_r**2

print(deimos_g)

earth_g = const.g_const * const.earth_r / const.earth_r**2

deimos_depth = (const.g_const * deimos_m) / (earth_g * deimos_r)

print("Problem A: " + str(deimos_depth))

# https://www.explainxkcd.com/wiki/index.php/681:_Gravity_Wells

# Problem D

geo_h = 35786 * 1000  # km

dist = const.earth_r + geo_h

v_esc = math.sqrt(2*const.earth_mu/dist)

v_esc_km = v_esc/1000

print("Problem D: " + str(v_esc_km))


# Problem E

pluto_m = 1.3e22  # kg
pluto_r = 1200 * 1000  # km

esc_v = math.sqrt(2*const.g_const*pluto_m/pluto_r)

esc_v_km = esc_v/1000

print("Problem E: " + str(esc_v_km))

# Problem I

hubble_d = 555 * 1000  # km - m

dist = const.earth_r + hubble_d

v_circ = math.sqrt(const.earth_mu/dist)

v_circ_km = v_circ/1000

print("Problem I: " + str(v_circ_km))
