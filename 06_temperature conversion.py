temperature = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Fahrenheit? (C or F): ").upper()

if unit == "C":
    temperature = (temperature * 9/5) + 32
    print(f"The temperature is: {round(temperature,1)} °F")

elif unit == "F":
    temperature = (temperature - 32) * 5/9
    print(f"The temperature is: {round(temperature,1)} °C")

else:
    print(f"{unit} was an invalid unit")