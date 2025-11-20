FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# 1️⃣ Define the functions first
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# 2️⃣ Main script
try:
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == "C":
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    elif unit == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    else:
        print("Invalid temperature. Please enter C or F")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
