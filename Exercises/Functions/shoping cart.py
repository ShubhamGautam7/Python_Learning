def main():
    price = float(input("what is the price? "))
    quantity = int(input("what is the quantity? "))
    discount_input = input("Discount Percentage? (leave blank for none): ")

    subtotal = calculate_subtotal(price, quantity)
    if subtotal is None:
        print("invalid quantity")
    elif discount_input:
        discount_per = float(discount_input)
        total = apply_discount(subtotal, discount_per)
        if total is None:
            print("Invalid Discount Percdntage!!")
        else:
            print(f"Yout total is {total:.2f}")
    else:
        total = apply_discount(subtotal)
        print(f"Yout total is {total:.2f}")




def calculate_subtotal(price, quantity):
    if quantity <= 0:
        return None
    else:
        return (price * quantity)
    
def apply_discount(subtotal, discount_per = 0):
    if discount_per < 0 or discount_per > 100:
        return None
    else:
        return (subtotal - (subtotal * discount_per / 100))
    


main()