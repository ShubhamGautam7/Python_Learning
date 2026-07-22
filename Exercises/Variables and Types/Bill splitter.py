bill = (input("what is the bill amount? "))
tip = (input("what percentage would like to tip? "))
people = int(input("how many of you are there? "))


bill = bill.replace('$' , '').replace('Rs' , '')
tip = tip.replace('%' , '')


bill = float(bill)
tip = float(tip)


tip_total = (tip/100) * bill
bill_total = tip_total + bill
per_person = bill_total / people


print(f"{'bill:':<15}${bill:8.2f}")
print(f"{'tip(' + str(int(tip)) + '%):':<15}${tip_total:8.2f}")
print(f"{'total:':<15}${bill_total:8.2f}")
print(f"{'per person:':<15}${per_person:8.2f}")