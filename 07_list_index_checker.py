animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"] 
try:
    ind = int(input("Enter an index: "))
    print(animals[ind])
except ValueError:
    print("Must be an integer")
except IndexError:
    print("Index out of range")