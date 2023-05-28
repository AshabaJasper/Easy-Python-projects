def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

#change
if unit.upper() == "C":
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temp))
elif unit.upper() == "F":
    print("Temperature in Celsius:", fahrenheit_to_celsius(temp))
else:
    print("Please enter correct unit (C/F)")
