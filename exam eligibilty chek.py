medical_cause = input("did you have a medical yes or no")
atten = int(input("Enter the attendance of the student: "))
if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten >= 75:
        print("You are allowed ")
    else:
        print("you are not allowed")