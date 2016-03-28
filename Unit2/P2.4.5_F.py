import math
from Constants import constants as const

sat_ecc = 0.3
sat_apo = 20000 * 1000  # m

r_p = sat_apo * ((1-sat_ecc)/(1+sat_ecc))

a = sat_apo / (1 + sat_ecc)

v_firstmember =  2 * const.earth_mu / r_p
v_secondmember = const.earth_mu / a

v = math.sqrt(v_firstmember - v_secondmember)

print(v/1000)