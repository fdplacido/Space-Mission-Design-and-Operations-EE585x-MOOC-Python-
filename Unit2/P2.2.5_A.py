deimos_m = 1.48e15  # kg
deimos_r = 6.2 * 1000  # km - m
g_constant = 6.67259e-11  # m^3*kg^-1*s^-2
earth_r = 6.378e6  # m
earth_m = 5.973e24  # kg

deimos_g = g_constant * deimos_m / deimos_r**2

print(deimos_g)

earth_g = g_constant * earth_m / earth_r**2

deimos_depth = (g_constant * deimos_m) / (earth_g * deimos_r)

print(deimos_depth)

# https://www.explainxkcd.com/wiki/index.php/681:_Gravity_Wells
