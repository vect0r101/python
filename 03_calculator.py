operator = input("Enter an operator (+, -, *, /): ")
num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: "))  

#we added int() to convert the input into an integer if we have not added int() then the input will be treated as a string and we will get an error while performing arithmetic operations on strings.

if operator == "+":
    result=num1+num2
    print(f"{num1} + {num2} = {result}")

elif operator == "-":
    result=num1-num2
    print(f"{num1} - {num2} = {result}")

elif operator == "*":
    result=num1*num2
    print(f"{num1} * {num2} = {result}")

elif operator == "/":
    result=num1/num2
    print(f"{num1} / {num2} = {result}")
    
else:
    print("Invalid operator")