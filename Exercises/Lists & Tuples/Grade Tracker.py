def main():
    grades =[]
    while True:
        score = input("Enter your score or 'done' to finish: ").lower().strip()
        if score.isdigit():
            score = int(score)
            x = add_grade(grades, score)
            if x is False:
                print("Invalid Grade, must be 0-100.")
        elif score == "done":
             break

    average = calculate_average(grades)
    if average is None:
         print("No grades Entered.")
    else:
         print(f"Your average grade is {average:.1f}")

    highest = get_highest(grades)
    if highest is None:
         print("No grades Entered.")
    else:
         print(f"Your highest score is {highest}.")

    lowest = get_lowest(grades)
    if lowest is None:
         print("No grades Entered.")
    else:
         print(f"Your lowest score is {lowest}.")

    

def add_grade(grades, score):
        if 0 <= score <= 100:
            grades.append(score)
            return True
        else:
            return False

def calculate_average(grades):
     if not grades:
          return None
     else:
          return(sum(grades)/len(grades))

def get_highest(grades):
     if not grades:
        return None
     else:
          return(max(grades))

def get_lowest(grades):
     if not grades:
        return None
     else: 
        return(min(grades))
                
        

main()
