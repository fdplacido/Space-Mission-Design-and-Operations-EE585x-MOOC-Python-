from Constants import constants as const
import math

# Δv_1 = sqrt((2μr_2)/(r_1(r_1+r_2))) - sqrt(μ/r_1)
# Δv_2 = sqrt((2μr_1)/(r_2(r_1+r_2))) - sqrt(μ/r_2)
# Δr/r = 4*ΔV/V
# Δr for leo = 3.5 Δv

# Problem A

del_r_LEO = 3.5  # Δv
altitude_increase = 10  # Km

delta_V_LEO = del_r_LEO / altitude_increase

print("Problem A: " + str(delta_V_LEO))

# Problem B

r_1 = (230 * 1000) + const.earth_r  # Km - m
r_2 = (20000 * 1000) + const.earth_r  # Km - m


def calc_v_1(r1, r2, mu):
    return math.sqrt((2 * mu * r2) / (r1 * (r1 + r2))) - math.sqrt(mu / r1)


def calc_v_2(r1, r2, mu):
    return math.sqrt((2 * mu * r1) / (r2 * (r1 + r2))) - math.sqrt(mu / r2)


v_1 = calc_v_1(r_1, r_2, const.earth_mu)
v_2 = calc_v_2(r_1, r_2, const.earth_mu)

print("Problem B: " + str(v_1 / 1000) + " and " + str(abs(v_2 / 1000)))

# Problem C

cape_canaveral_incl = 28.5  # degrees
sat_orb = (450 * 1000) + const.earth_r  # Km - m
geo_orb = (35785 * 1000) + const.earth_r  # Km - m

# V = sqrt(μ/r)
v_leo = math.sqrt(const.earth_mu/sat_orb)

v_geo = math.sqrt(const.earth_mu/geo_orb)

print("Problem C: ")
print("\tV_leo = " + str(v_leo/1000))
print("\tV_geo = " + str(v_geo/1000))
print("\tv_1 = " + str(calc_v_1(sat_orb, geo_orb, const.earth_mu)/1000))
print("\tv_2 = " + str(abs(calc_v_2(sat_orb, geo_orb, const.earth_mu)/1000)))
