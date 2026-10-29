try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"Answer: {num1/num2}")
except ZeroDivisionError:
    print("Cannot divide by 0")
except ValueError:
    print("Can only divide integers")