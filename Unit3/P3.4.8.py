from Constants import constants as const
import math

# Problem D

apogee_raise = 10  # Km
leo_factor = 3.5

# Δr = 3.5 Δv

v = apogee_raise/leo_factor

print("Problem D: " + str(v))

# Problem E

# ΔX = 3πΔr

space_suttle_delta_r = 12
space_suttle_alt = 400 - space_suttle_delta_r

x = 3 * math.pi * space_suttle_delta_r  # Km / orbit

orbits_needed = space_suttle_alt/x

print("Problem E: " + str(orbits_needed))

# Problem F

initial_alt = 210 * 1000  # km - m
final_alt = 590 * 1000  # km - m

final_orb = final_alt + const.earth_r
initial_orb = initial_alt + const.earth_r

# T = 2π sqrt(a^3/μ)

T = 2 * math.pi * math.sqrt(final_orb**3 / const.earth_mu)

T_min = T/60  # to minutes

print("Problem F: " + str(T_min/2))

# n = sqrt(μ/a^3)

n = math.sqrt(const.earth_mu/(final_orb**3))  # deg / s

degrees_travelled = n * T

print("Problem F_2: " + str(degrees_travelled))







