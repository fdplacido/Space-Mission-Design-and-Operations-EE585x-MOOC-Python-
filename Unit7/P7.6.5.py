from Constants import constants as const

sp_area = 8  # m^2
sp_effi = 0.3
tranmission_eff = 0.85

power = 1e6  # GW -> W

p_p = sp_area * const.solar_constant * sp_effi * tranmission_eff

n_p = power/p_p

print("Problem B: " + str(n_p))

