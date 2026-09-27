#our final goal is to show the weight in kg only 
""""
choose = str(input("choose weight metrics (kg/pounds): "))
weight = float(input("Enter the weight: "))

if choose != str("kg") and choose != str("pounds"):
    print("invalid input")

elif choose == "pounds":
    weight = weight * 0.453592
    print(round(weight,2), " kg")

else:
    print(round(weight,2)," kg" )
    
"""

#Mistakes / Improvements:

#1. Unnecessary use of str()
   #- input() already returns a string.
   #- "kg" and "pounds" are already strings.

#2. Condition can be simplified
   #- Instead of: choose != "kg" and choose != "pounds"
   #- Use: choose not in ("kg", "pounds")

#3. Case-sensitive input
   #- KG, Kg, POUNDS are treated as invalid.
   #- Use .lower() on input.

#4. Weight is asked before validating metric
   #- Program asks for weight even if metric is invalid.

#5. No handling for invalid weight input
   #- Entering text instead of a number causes ValueError.

#6. Extra space in output
   #- " kg" already contains a space and print() adds another.

#7. Repeated print statements
   #- Same print logic appears in multiple places.
    



choose = input("Choose weight metric (kg/pounds): ").lower()

if choose not in ("kg", "pounds"):
    print("Invalid input")
else:
    weight = float(input("Enter the weight: "))

    if choose == "pounds":
        weight = weight * 0.453592

    print(round(weight, 2), "kg")