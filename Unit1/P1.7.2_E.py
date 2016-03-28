import math

au = 150e6 * 1000 # km to m
S = 1368 # W/m^2
d_e = 1
d_j = 5.2
j_r = 50

S_j = S*(d_e/d_j)**2

result = S_j*math.pi*j_r**2

print(S_j)