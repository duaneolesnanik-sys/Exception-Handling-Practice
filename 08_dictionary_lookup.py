prices = {"pizza": 12, "burger": 8, "fries": 4, "soda": 2} 
try:
    item = input("What item are you looking for: ")
    print(f"That item costs ${prices[item]}")
except KeyError:
    print("That item doesn't exist")