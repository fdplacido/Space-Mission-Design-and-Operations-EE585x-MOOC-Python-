from Constants import constants as const
import math

# Problem A

iss_alt = 400 * 1000  # Km - m
sshuttle_apo =  400 * 1000  # Km - m
sshuttle_per = 370 * 1000  # Km - m

# ΔX = 3πΔr

alt_diff = const.earth_r + iss_alt - (const.earth_r + (sshuttle_apo + sshuttle_per)/2)

x = 3 * math.pi * alt_diff

print("Problem A: " + str(x/1000))

# Δr = 3.5Δv
per_raise = 10  # Km - m

v = per_raise / 3.5

print("Problem A_2: " + str(v))

# Problem F

sideral_day_secs = 4
sideral_day_min = 56
sideral_day_hour = 23

sideral_day_in_secs = sideral_day_secs + sideral_day_min*60 + sideral_day_hour*(60*60)

geo_orbit =  (const.earth_mu*(((sideral_day_in_secs)/(2 * math.pi))**2))**(1/3)

print("Problem F: " + str(geo_orbit))

# Problem G

alt_per = 350 * 1000  # Km - m
alt_apo = 400 * 1000  # Km - m
final_circ_orbit = 400  # Km

orbit_per = alt_per + const.earth_r
orbit_apo = alt_apo + const.earth_r
a = orbit_per + orbit_apo

# Hohmann transfer
# Δv_2 = - sqrt((2μr_1)/(r_2(r_1+r_2))) + sqrt(μ/r_2)

v_2 = -1 * math.sqrt((2 * const.earth_mu * orbit_per)/(orbit_apo * a)) + math.sqrt(const.earth_mu/orbit_apo)

print("Problem G: " + str(v_2))

