import math

# Take angle input in degrees
angle_deg = float(input("Enter angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate sin, cos, tan
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)

# Handle the case when cos(angle) = 0 (tan is undefined)
try:
    tan_val = math.tan(angle_rad)
except:
    tan_val = "Undefined (cos = 0)"

# Display results
print(f"sin({angle_deg}°) = {sin_val}")
print(f"cos({angle_deg}°) = {cos_val}")
print(f"tan({angle_deg}°) = {tan_val}")