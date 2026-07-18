import sys
import time

def print_slow(text):
    """A function to print with a delay for a retro feel"""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
while True:

    print_slow("----------Simple interest finder----------")

    P = float(input("state your amount of money: "))
    T = float(input("state your amount of time to put your money: "))
    R = float(input("state your amount of percentage of interest: "))

    if T < 0:
        print_slow("Please enter a number that is above 0")

    elif P == 0:
        ValueError

    elif R == 0:
        print_slow("Please enter a number that is above 0")

    SI = ((P*T*R)/100)
    print_slow(f"Your amount of money in {T} years is ${SI}")

    
    
    Choice = input("Do you want to continue? (Y/n)")

    if Choice == "y" or "Y":
        continue

    elif Choice == "n" or "N":
        break

    else:
        print_slow("invalid choice")
        break