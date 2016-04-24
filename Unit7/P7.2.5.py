sat_m = 2000  # Kg
sat_r = 1.1  # m
sat_length = 4  # m
sat_rot = 1  # rpm

astr_thrust_n = 2
astr_thrust_power = 10.6  # N
astr_thrust_location = 0.5  # m
astr_m = 250  # Kg

# α = nFL/I
# I = mr^2/2
# ω = αt

sat_spacew_m = sat_m + astr_m

I = (sat_spacew_m*(sat_r**2))/2
t = (sat_r * I)/(2 * astr_thrust_n * astr_thrust_power * astr_thrust_location)

print("Problem G: " + str(t) + " still wrong...")