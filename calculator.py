def add (P, Q):
    return P+Q

def add (P, Q):
    return  P  -  Q

def add (P, Q):
    return  P * Q

def add (P, Q):
    return  P / Q
#now we take inputs from the user
print(" Please select an oparation.")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")

choice = input("please enter choice (a/b/c/d):")

num_1 = int(input(" please enter the first number: "))
num_2 = int(input(" please enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", add(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", add(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", add(num_1, num_2))
else:
    print("this is an invalid input")
