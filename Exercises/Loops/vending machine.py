
amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Incert Coin: "))

    if coin in [25, 10, 5, 1 ]:
        amount_due -= coin
            
print(f"Change owed: {abs(amount_due)}")


