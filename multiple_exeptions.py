try:
    num1, num2 = eval(input("Enter two numbers, serperated by a comma:  "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is an error!! ")
except SyntaxError:
    print("Comma is missing. Enter numbers serperated by coma like 1,2 ")
except:
    print("Wrong put")
else:
    print("No exeptions")
finally:
    print("This will exicute no matter what")