import math

proton_s = 300000 * 1000 # m/s

proton_alt = 100 * 1000 # m
earth_r = 6.378e6 # m
landa = 90 * math.pi / 180# degrees to rads
B_zero_eq = 3.12e-5 # Tesla

proton_dist = 1 + proton_alt/earth_r

first_member = math.sqrt(1 + 3*(math.sin(landa))**2) # (1 + 3*sin^2*λ)^(1/2)
second_member = B_zero_eq/(proton_dist**3)

B = first_member * second_member

print(B)
