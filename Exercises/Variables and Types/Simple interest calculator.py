p = float(input("principal? "))
r = float(input("rate? "))
t = float(input("time? "))
i = (p * t * r) / 100 
print(f"simple interest is {i : .2f}")
total = p + i
print(f"total is {total:.2f}")