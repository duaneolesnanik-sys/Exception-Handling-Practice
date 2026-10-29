prices = []
while True:
    user = input("Enter item price (Q to quit): ")
    if user.strip().lower() == "q":
        print("Entry processed")
        break
    else:
        try:
            prices += [float(user)]
            print("Item added")
        except ValueError:
            print("Invalid price")
    print("Entry processed\n")
print(f"Items purchased: {len(prices)}\nTotal: ${sum(prices)}")