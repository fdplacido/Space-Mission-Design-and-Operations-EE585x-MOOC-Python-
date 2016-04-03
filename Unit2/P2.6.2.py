import math

r_fg3 = 700  # m
mu_fg3 = 140.15  # m^3/s^2
spacecraft_alt = 1.5 * 1000  # m
ast_r = 700  # m

# V_circular_orbit
spacecraft_v = math.sqrt(mu_fg3/(spacecraft_alt + ast_r))

print("Spacecraft speed: " + str(spacecraft_v))

# 2nd question

spacecraft_periap = 10  # m
spacecraft_apoaps = spacecraft_alt + ast_r

# a = (r_a + r_p) / 2
semimajoraxis = (spacecraft_apoaps + spacecraft_periap) / 2

# e = (r_a / a) - 1
eccentricity = (spacecraft_apoaps / semimajoraxis) - 1

# cosθ = ( a (1 - e^2) / re ) - 1/e
cos_true_anomaly = ((semimajoraxis * (1 - eccentricity ** 2)) / (ast_r * eccentricity)) - (1 / eccentricity)
true_anomaly_rad = 2*math.pi - math.acos(cos_true_anomaly)
true_anomaly_deg = 360 - math.degrees(true_anomaly_rad)

# cosE = (e + cosθ) / (1 + e cosθ)
cos_eccentric_anomaly = (eccentricity + cos_true_anomaly) / (1 + eccentricity * cos_true_anomaly)

# n = sqrt(mu / a^3)
n = math.sqrt(mu_fg3/semimajoraxis**3)

# time since periapsis
# t = (E - e sin(E)) / n
E = math.acos(cos_eccentric_anomaly)
t_intersection = (E - eccentricity * math.sin(E)) / n

period = 2 * math.pi * math.sqrt(semimajoraxis**3/mu_fg3)

t_apoapsis = period/2

t_elapsed_since_apoapsis = t_apoapsis - t_intersection

print("Time elapsed since apoapsis: " + str(t_elapsed_since_apoapsis/(60*60)))  # in hours

# 3rd question

# V = sqrt((2μ/r) - (μ/a))

land_vel = math.sqrt((2*mu_fg3/ast_r) - (mu_fg3/semimajoraxis))

print("Landing velocity: " + str(land_vel))

# 4th question

# flight path angle => tan(φ) = (e sin(Θ))/(1 + e cos(Θ))

path_angle = math.atan((eccentricity * math.sin(true_anomaly_rad))/(1 + (eccentricity * math.cos(true_anomaly_rad))))
path_angle_deg = math.degrees(abs(path_angle))

print("Flight path angle: " + str(path_angle_deg))

# 5th question

# the time to go up and down
print("Time to touch down again: " + str(2*t_elapsed_since_apoapsis/(60*60)))

