import math

r_fg3 = 700  # m
mu_fg3 = 140.15  # m^3/s^2
spacecraft_alt = 1.5 * 1000  # m

spacecraft_v = math.sqrt(mu_fg3/r_fg3)

print(spacecraft_v)

# 2nd question

spacecraft_periap = 10  # m
spacecraft_apoaps = spacecraft_alt

# a = (r_a + r_p) / 2
semimajoraxis = (spacecraft_apoaps + spacecraft_periap) / 2

# e = (r_a / a) - 1
eccentricity = (spacecraft_apoaps / semimajoraxis) - 1

# cosθ = ( a (1 - e^2) / re ) - 1/e
true_anomaly = ( (semimajoraxis * (1 - eccentricity**2))/(spacecraft_periap*eccentricity) ) - (1/eccentricity)

# cosE = (e + cosθ) / (1 + e cosθ)
eccentric_anomaly = (eccentricity + true_anomaly) / (1 + eccentricity * true_anomaly)

# n = sqrt(mu / a^3)
n = math.sqrt(mu_fg3/semimajoraxis**3)

# time since periapsis
# t = (E - e sin(E)) / n
E = math.acos(eccentric_anomaly)
t = (E - eccentricity * math.sin(E)) / n

print(eccentricity)

print(t)


