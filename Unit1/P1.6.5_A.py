iss_m = 450 * 1000 # tonnes to kg
iss_surface = 1500 # m^2
iss_orbit = 400 * 1000 # km to m
drag_c = 2

BC = iss_m / (drag_c*1500)

print(BC)