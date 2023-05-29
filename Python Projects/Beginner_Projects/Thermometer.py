def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    temp_input = input("Enter the temperature (or 'q' to quit): ")
    
    if temp_input.lower() == 'q':
        break

    try:
        temp = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a number.")
        continue

    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()

    if unit == "C":
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temp))
    elif unit == "F":
        print("Temperature in Celsius:", fahrenheit_to_celsius(temp))
    else:
        print("Please enter correct unit (C/F)")
