from Constants import constants as const
import math

# Problem B

m_rosseta = 3000  # kg
isp = 220  # s

earth_g = const.earth_mu / (const.earth_r**2)

v = earth_g * isp * math.log(m_rosseta/(m_rosseta/2))

print("Problem B: " + str(v/1000))

v = 100  # m/s

m_100 = m_rosseta * math.pow(math.e, (-v/(earth_g*isp)))

print("Problem B_2: " + str(m_100))

# Problem C

max_w = 10.45  # tones

fs_dry_m = 20  # tones
fs_wet_m = 260  # tones

fs_isp_0 = 282  # s
fs_isp_vacuum = 311  # s

ss_dry_m = 3
ss_wet_m = 53
ss_isp = 342

payload = 10  # tones

fs_masses = (fs_wet_m + ss_wet_m + payload) / (fs_dry_m + ss_wet_m + payload)
v_1 = earth_g * fs_isp_vacuum * math.log(fs_masses)

ss_masses = (ss_wet_m + payload) / (ss_dry_m + payload)
v_2 = earth_g * ss_isp * math.log(ss_masses)

v_final = v_1 + v_2

print("Problem C: " + str(v_final/1000))

dry_m = 23
wet_m = 313
isp = 342

masses = (wet_m + payload) / (dry_m + payload)
v = earth_g * isp * math.log(masses)

print("Problem C_2: " + str(v/1000))
