print("-" * 30 + "CALCULATOR" + "-" * 30)
print("-" * 70)

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. remainder")
print("6. odd or even")
print("7. power")
print("8. square")
print("9. square root")
print("10. exit")

print("Enter a number from 1 to 10")

while True:

    choice = int(input("Enter your choice: "))

    if choice < 1 and choice > 10:
        print("Invalid choice, please enter a number from 1 to 10")

    if choice == 1:
        num1 = float(input("Give your first number: "))
        num2 = float(input("Give another number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")

    elif choice == 2:
        num1 = float(input("Give your first number: "))
        num2 = float(input("Give another number: "))
        result = num1 - num2
        print(f"The subtraction of {num1} and {num2} is {result}")

    elif choice == 3:
        num1 = float(input("Give your first number: "))
        num2 = float(input("Give another number: "))
        result = num1 * num2
        print(f"The multiplication of {num1} and {num2} is {result}")

    elif choice == 4:
        num1 = float(input("Give your first number: "))
        num2 = float(input("Give another number: "))
        result = num1 / num2
        print(f"The division of {num1} and {num2} is {result}")

    elif choice == 5:
        num1 = float(input("Give your first number: "))
        num2 = float(input("Give another number: "))
        result = num1 % num2
        print(f"The remainder of {num1} divided by {num2} is {result}")

    elif choice == 6:
        num1 = float(input("Give a number: "))
        if num1 % 2 == 0:
            print("The number is even!")
        else:
            print("The number is odd!")
    
    elif choice == 7:
        num1 = float(input("Give a number: "))
        power = float(input("Give a number to power the input number: "))
        result = num1 ** power
        print(f"The square of {num1} is {result}")

    elif choice == 8:
        num1 = num1 = float(input("Give a number: "))
        result = num1 ** 2
        print(f"The square of {num1} is {result}")

    elif choice == 9:
        num1 = float(input("Give a number: "))
        result = num1 ** 0.5
        print(f"The square root of {num1} is {result}")

    elif choice == 10:
        print("done!")
        break

    else:
        print("i don't understand that")