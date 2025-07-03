print("enter a number (numerator):")
numn= int(input())
print("enter an number (denominator): ")
denom=int(input())
if numn%denom == 0:
    print("\n"+str(numn) + "is divisble by "+ str(denom))
else:
    print("\n" +str(numn) + " is not divisble by "+str(denom))