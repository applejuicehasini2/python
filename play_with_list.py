L = [4,5,1,2,9,7,10,8]
print("Original list : ", L)
count = 0
for i in L :
    count += i
avg = count/len(L)
print("sum =  ", avg)
print("Avarage = ", avg)
L.sort()
print("The smallest element is: ", L[0])
print ("The largest element is: ",L[-1])