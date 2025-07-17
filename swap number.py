
# Swapping three numbers cyclically: a → b, b → c, c → a

a = int(input("Enter first number (a): "))

b = int(input("Enter second number (b): "))

c = int(input("Enter third number (c): "))

print("\nBefore swapping:")

print("a =", a)

print("b =", b)

print("c =", c)

# Cyclic swap

a, b, c = c, a, b

print("\nAfter swapping (cyclic):")

print("a =", a)

print("b =", b)

print("c =", c)