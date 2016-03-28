import math

cubesat_h = 10 / 100 # cm to m
cubesat_m = 0.8
C_d = 2.2
iss_c_d = 150

cubesat_surface = 6 * cubesat_h**2

print(cubesat_surface)

sphere_eq_radius = math.sqrt(cubesat_surface / (4 * math.pi)) # 4 pi r^2 = S

cubesat_cross_section = math.pi * sphere_eq_radius**2

print(cubesat_cross_section)

ballistic_coef_cubesat = cubesat_m / (C_d * cubesat_cross_section)

print(ballistic_coef_cubesat)

cubesat_m_like_iss = iss_c_d * (C_d * cubesat_cross_section)

print(cubesat_m_like_iss)