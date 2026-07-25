def main():
    temp = float(input("enter temperature: "))
    con = input("convert to fahrenheit (Enter f) convert to celsius (enter c) ").lower()

    if con == "f":
        x = celsius_to_fahrenheit(temp)
        if x is None:
            print("That temperature is physically impossible.")
        else:
            print(f"{temp}°C is {x:.2f}°F")
    elif con == "c":
        x = fahrenheit_to_celsius(temp)
        if x is None:
            print("That temperature is physically impossible.")
        else:
            print(f"{temp}°F is {x:.2f}°C")
    else:
        print("Try again")
    print()
    
def celsius_to_fahrenheit(c):
    if c < -273.15:
        return None
    else:
        return((c * 9/5) + 32)

def fahrenheit_to_celsius(f):
    a = (f - 32) * 5/9
    if a < -273.15:
        return None
    else :
        return a 

main()