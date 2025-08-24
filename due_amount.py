p = float(input("Enter your bill amount: "))
x = float(input("Enter your paying amount: "))
if x < 2.50:
    print("PLEASE CHOOSE A AMOUNT MORE THAN 2.50")
elif x == p :
    print("Is the same amount")
else:
    print("Your change:")
    print(x - p)