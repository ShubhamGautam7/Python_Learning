#If age is 18 or older → "Access granted."
#If age is under 18 AND a guardian is present → "Access granted with supervision."
#If age is under 18 AND no guardian is present → "Access denied."

age = int(input("enter your age: "))

if age >= 18 :
    print("Access Granted")
    
elif age < 18 :
    guardian = input("is your guardian present? ").lower()

    if guardian == "yes" :
            print("Access granted with supevision")

    elif guardian == "no" :
            print("Access denied")
    
    elif guardian not in ("yes" , "no") :
            print("invalid input")