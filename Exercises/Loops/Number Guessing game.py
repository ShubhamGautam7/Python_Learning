secret = 31
for i in range (1,6):
    print(f"Attempt {i} of 5.")
    a = int(input("enter your guess: "))
    if a > secret:
        print("guess is greater")
    elif a < secret:
        print("guess is lower")
    else:
        print("CORRECT GUESS. CONGURATUATION")
        break
else:
    print(f"out of attempts. the number was {secret}")