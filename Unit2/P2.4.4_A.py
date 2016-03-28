earth_mu = 3.986e14
earth_r = 6.378e6  # m
speed = 7.76 * 1000  # m/s

# V = sqrt(mu/r) => V^2 = mu/r => V^2/mu = 1/r
# mu / V^2 = r

dist = earth_mu / (speed**2)
dist = dist - earth_r

print(dist/1000)
