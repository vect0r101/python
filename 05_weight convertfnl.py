
weight = float(input("Enter the weight: "))
unit = input("kilogram or pounds? (k or l): ").lower()

if unit == "k":
    weight= (weight * 2.205)
    unit = "lbs"
    print(f"Your weight is: {round(weight,1)} {unit}")


elif unit == "l":
    weight = (weight / 2.205)
    unit = "kg"
    print(f"Your weight is: {round(weight,1)} {unit}")

    
else:
    print(f"{unit} was invalid unit" )


#here after every else it statements we added print because if the user enters an invalid unit then we want to show the user that the unit they entered is invalid. If we do not add print statement after else then the program will not show any message to the user and it will just end without any output which can be confusing for the user.
