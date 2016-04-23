# Problem A

alt = 296  # Km
tether_long = 20  # Km
earth_magnetic_field = 3e-5  # T

space_shuttle_m = 100 * 1000  # T - Kg
sat_m = 500  # Kg

h_ss = alt - 0.1

print("Problem A: " + str(h_ss))

# m_sat * d_sat = m_ss * d_ss

d_sat = (space_shuttle_m/sat_m) * (tether_long/201)

# h_sat = h_cm - 0.1
# h_cm = + d_sat

h_sat = alt + d_sat

print("Problem A2: " + str(h_sat))

angle = 30

# U_i = (v x B) * l

# TODO
