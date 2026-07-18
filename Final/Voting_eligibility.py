import sys
import time

def print_slow(text):
    """A function to print with a delay for a retro feel"""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

print_slow("----------Voting eligibility----------")

age = int(input("State your age for the voting system: "))

if age >= 18:
    print_slow("You are eligible for the voting, Please proceed")

elif age < 18:
    print_slow("Sorry but you are not eligible for the voting")

else:
    print_slow("How did you get here?")