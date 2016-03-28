# F = (G*M*m)/r^2
# Equal forces
# mu_earth / d_1^2 = mu_sun / d_2^2 ->
# mu_earth / mu_sun = (d_1 / d_2)^2 ->
# sqrt(mu_earth / mu_sun) = d_1/d_2 ->
#

import math

mu_earth = 3.986e14  # m^3 / s^2
mu_sun = 1.327e20  # m^3 / s^2
astronomical_unit = 1.496e11  # m

distances_relation = math.sqrt(mu_earth/mu_sun)
d_earth = distances_relation*astronomical_unit

print(d_earth / 1000)  # To Km


d_earth_2 = astronomical_unit / (1 + (math.sqrt(mu_sun/mu_earth)))
print(d_earth_2 / 1000)  # To Km
