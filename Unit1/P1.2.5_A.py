import math

m_cass = 5600   # cassini -- kg
h_cass = 5      # m
d_cass = 2      # m
rpm_cass = 1    # rpm
dps_cass = 6    # degrees per second
m_ant = 50      # antenna mass -- kg
l_ant = 10      # antenna length -- m


# Angular momentum: L for a solid body, with fixed rotation axis Δ
# L = IΔ * ω --- ω = rotation

# Moment of inertia: wher r is the distance of the mass element to the axis of rotation
# IΔ = ∫∫∫r²ρ (r)dV --- or IΔ = Σmr² 
# ρ = M/V (density = Mass / Volume)
# Making the integral for the Cylinder gives us:
# I_cylinder = (1/2)MR²

# Momentum conservation
# L_a = L_b => IΔ_a * ω_a = IΔ_b * ω_b

r_cass = d_cass / 2         # cassini radius
r_ant = r_cass + l_ant  # antenna radius to the center when deployed

# moment of inertia - a
I_a = (1/2 * m_cass * math.pow(r_cass,2)) + (2*m_ant * math.pow(r_cass,2)) # kg*m²

# angular momentum - a
L_a = I_a * dps_cass # kg*m²*deg/s

# moment of inertia - b
I_b = (1/2 * (m_cass) * math.pow(r_cass,2)) + (2*m_ant * math.pow(r_ant,2))

# Getting rotation speed for b: L_a = IΔ_b * ω_b => ω_b = L_a / IΔ_b
dps_deployed = L_a / I_b

print(dps_deployed)