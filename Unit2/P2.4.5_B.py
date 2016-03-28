from Constants import constants as const

earth_ecc = 0.0167
earth_semi_major_axis = 1.000001018  # AU

# a = r_p / (1 - e)
# a = r_a / (1 + e)

r_p = earth_semi_major_axis * (1 - earth_ecc)
r_a = earth_semi_major_axis * (1 + earth_ecc)

difference = r_a - r_p

difference = difference * const.astronomical_unit

print (difference/1000)  # km