import math

amplitude = 6.2  # Km/s
deflection = 27  # deg
v_before = 37.4  # Km/s

# v_before = v_after

print("Problem A: " + str(amplitude))

total_deg = 90 + deflection

# v_after^2 = V_v^2 + v_a_inf^2 - 2V_v*v_a_inf*cos(angle)
# V_v^2 = V^before^2 - v_a_inf^2
# v_after^2 = v_before^2 - 2 * sqrt(v_before^2 - v_a_inf^2) * v_a_inf * cos(gamma)

v_after_square = v_before**2 - 2 * math.sqrt(v_before**2 - amplitude**2) * amplitude * math.cos(total_deg)
v_after = math.sqrt(v_after_square)

print("Problem B: " + str(v_after))