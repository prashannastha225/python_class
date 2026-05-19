import sys
import time

def print_slow(text):
    """A function to print with a delay for a retro feel"""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

celsius = float(input("state your temperature in celsius: "))
fahrenheit = float(input("state your temperature in fahrenheit: "))
fahrenheit = (celsius * 9/5) + 32
celsius = (fahrenheit - 32) * 5/9
print_slow(f"the degree in fahrenheit is {fahrenheit}")
print_slow(f"the degree in celsius is {celsius}")