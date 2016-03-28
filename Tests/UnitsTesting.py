from astropy import units as u

# Astropy package for units conversion

S = 1.4 * u.kW / u.m ** 2

print(S)

print(S.to(u.W / u.m ** 2))