import math
def circumference(radius):
    return 2 * math.pi* radius
r = float(input("Enter the radius of the circle"))
print(f"Ther circumference of a circle with radius {r} is {circumference(r):.2f}")
