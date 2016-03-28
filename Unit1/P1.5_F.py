import math

h = 2
r = 0.5
alpha = 0.2

S = 1.4 # k*W/m^2
stef_boltz = 5.67e-8 # W/(m^2*K^4)


def cylinderSurface(height, radius):
    return (2 * math.pi * math.pow(radius, 2)) + (2 * math.pi * radius * height)

def cylinderExposedSurface(height, radius):
    return 2 * radius * height

result = (alpha * S * cylinderExposedSurface(h,r) * 1000)

print(result)

