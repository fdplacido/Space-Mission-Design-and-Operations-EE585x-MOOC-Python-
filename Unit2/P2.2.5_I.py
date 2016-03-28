import math
import os

os.path.realpath(__file__)

hubble_d = 555 * 1000  # km - m
earth_mu = 3.986e14  # m^3*s^-2
earth_r = 6.378e6  # m

dist = earth_r + hubble_d

v_circ = math.sqrt(earth_mu/dist)

v_circ_km = v_circ/1000

print(v_circ_km)
