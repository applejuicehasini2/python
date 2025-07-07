print("select your bike ride : ")
print("1. bike")
print("2. car")
choice= int (input("enter your choise : "))
if(choice == 1):
    print("what tipe of bike ?")
    print("1. Scooty\n")
    print("2.scooter\n")
    choice2 = int(input("enter yor choice2: "))
    if choice2 ==2 == 1 :
        print ("you have selected scooty")
    else:
        print("you have selected scooter")
elif(choice == 2):
    print("has that type of car ?")
    print("1. sedan")
    print("2. XUV")
    choice3= int(input("Enter your choice3"))
    if choice3 == 1 :
        print("you have selected sedan")
    else:
        print("you have selected XUV")
else:
    print("wrong choice!")
