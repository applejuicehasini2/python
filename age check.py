age = int(input("Enter your age: "))  # Convert input to integer

def is_odd(num):
    return num % 2 != 0

if is_odd(age):
    print("odd number")
else:
    print("even number")
