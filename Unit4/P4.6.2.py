from Constants import constants as const
import math

# Problem A

probe_dist = 133.9 * const.astronomical_unit # AU -> m
probe_v = 17 * 1000  # Km /s -> m/s

# Energy conservation

v_square = (probe_v**2) + (2 * const.sun_mu) * ((1/const.astronomical_unit) - (1/probe_dist))
v = math.sqrt(v_square)

print("Problem A: " + str(v/1000))

# Problem B

jupiter_orbit_r = 5.204 * const.astronomical_unit  # AU -> m
jupiter_m = 1.8987e27  # Kg
jupiter_r= 69911  # Km

# Hohmann transfer

semi_major_a = (const.astronomical_unit + jupiter_orbit_r)/2
V = math.sqrt((2*const.sun_mu/const.astronomical_unit) - (const.sun_mu/semi_major_a))

# v_d = V - V_earth

v_d = V - math.sqrt(const.sun_mu/const.astronomical_unit)

print("Problem B: " + str(v_d/1000))

# Problem B_2

alt = 200 * 1000 # Km -> m
dist = alt + const.earth_r

# escape velocity

v_esc = math.sqrt((2*const.earth_mu)/(dist))

# v_depart^2 = v_dept_infty^2 + v_esc^2

v_depart_sqrt = v_d**2 + v_esc**2
v_depart = math.sqrt(v_depart_sqrt)/1000


print("Problem B_2: " + str(v_depart))

# Problem B_3

# e = v^2/2 - mu/r

e = (v_d**2)/2

print("Problem B_3: " + str(e/(1000*1000)))

# Problem B_4

# e = v^2/2 - mu/r
# v = sqrt(2mu/r - mu/a)

v = math.sqrt((2*const.earth_mu/dist) - (const.earth_mu/semi_major_a))

energ = (v**2)/2 - const.sun_mu/jupiter_orbit_r

energ = -const.sun_mu/(2*semi_major_a)

print("Problem B_4: " + str(energ/(1000*1000)))

# Problem B_5

# using the period

T = math.pi * math.sqrt((semi_major_a**3)/const.sun_mu)
T = T/(60 * 60 * 24)  # s -> days

print("Problem B_5: " + str(T))

# Problem B_6

v_arrival = math.sqrt((2*const.sun_mu/jupiter_orbit_r) - (const.sun_mu/semi_major_a))

v_arrival_excess = v_arrival - math.sqrt(const.sun_mu/jupiter_orbit_r)

print("Problem B_6: " + str(v_arrival_excess/1000))

# Problem B_7

impact = 100000 * 1000  # Km -> m

v_esc = math.sqrt(2 * const.jupiter_mu / impact)
v_esc /= 1000

v_p = math.sqrt(v_esc**2 + v_arrival_excess**2)

print("Problem B_7: " + str(v_p/1000))

# vp^2 = v_esc^2 + v_a^2

# Problem C

msl_mass = 4050  # Kg
msl_alt = 200 * 1000  # Km
orb_vel = 7.78 * 1000  # Km/s
v_depart = 11.50 * 1000 # Km/s
isp = 320  # s
m_exp = 5  # Kg/s

# Tsiolkovsky

# v = g * Isp * log (m / (m - mt))

earth_g = const.earth_mu / (const.earth_r**2)
first_m = earth_g * isp

t = (msl_mass * (1 - math.exp(-orb_vel/first_m))) / m_exp

print("Problem C: " + str(t))

