score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print(f"Score: {score} ---> Invalid")

elif score >= 90 :
    print(f"Score: {score} ---> Grade: A")

elif score >= 80 :
    print(f"Score: {score} ---> Grade: B")

elif score >= 70 :
    print(f"Score: {score} ---> Grade: C")

elif score >=60 :
    print(f"Score: {score} ---> Grade: D")

else :
    print(f"Score: {score} ---> Grade: F")