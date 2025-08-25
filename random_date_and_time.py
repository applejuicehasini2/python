import random
import time
def getRandomDate(startDate, endDate):
    print("Print random date between", startDate, "and" , endDate)
    randomGenarator = random.random()
    dateFormat = '%m/%d/%y'
    starTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate,  dateFormat))
    randomTime = starTime + randomGenarator * (endTime - starTime)
    randomDate =time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("Random Date = ", getRandomDate("1/1/2000", "12/12/2025"))