def main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    
    if op == "+":
        result = add(x, y)
        print(result)

    elif op == "-":
        result = subtract(x, y)
        print(result)

    elif op == "*":
        result = multiply(x,y)
        print(result)

    elif op == "/":
        result = divide(x, y)

        if result is None:
            print("cannot be divided by zero")
        else:
            print(result)
            
    else:
        print("invalid Operator")

def add(a, b):
    return (a+b)
    
def subtract(a, b):
    return (a-b)
    
def multiply(a ,b):
    return (a*b)
    
def divide(a, b):
    if b == 0:
        return None
    else:
        return (a/b)

main()