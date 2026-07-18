import sys
import time
import random
def print_slow(text):
    """A function to print with a delay for a retro feel"""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
attempt=0
while attempt<=2:
    print_slow("-----welcome to the number guessing game!-----")
    print_slow("Here you try to guess the number!\n")
    print_slow("Here it goes! guess the number!")
    rand_int=random.randint
    choice=int(input(">"))
    if choice==rand_int:
        print_slow("Wow! you did in the first try! lucky guy")
    else:
        print_slow(f"Well, better luck next time! The number was {rand_int}")
    attempt+=1