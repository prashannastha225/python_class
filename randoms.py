import time
import sys
import random

# THE TERMINAL OBLIVION SCRIPT 🥀😭
while True:

    def print_slow(text):
        """A function to print with a delay for a retro feel"""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

    user_input = input("Critical System Error detected. Repair? (yes/no): ").lower().strip()
    
    if "yes" in user_input:
        print("Initializing repair...")
        time.sleep(1)
        print("Error: Brain cells not found. 🧠💨")
        print("Reverting 'yes' to 'no'. User is clearly hallucinating.")
        
    elif "no" in user_input:
        for i in range(1, 6):
            print(f"Purging: C:/Windows/System32/drivers/driver_{i}.sys ... [OK]")
            time.sleep(0.4)
        print("CRITICAL: OS kernel has left the chat. ✌️💀")
        
        print("User declined repair. Executing 'Spite Protocol'...")
        time.sleep(1)
        for i in range(1, 4):
            print(f"Purging: C:/Windows/System32/boot_sector_{i}.bak ... [OK]")
            time.sleep(0.5)
        
        print("\nFATAL: System stability at 1%. 🧠🧨")
        print("Automatic self-destruct initiated to save the motherboard...")
        
        # The fake countdown that breaks souls
        for i in range(10, 0, -1):
            print("Hacking Teacher_PC_Admin... [SUCCESS] ✅")
            print("Accessing 'Grades_Final_Final_v2.xlsx'... 🤡")
            time.sleep(1)
            print(f"TERMINATING IN {i}... 🥀", end="\r")
            time.sleep(1)
        
        print("\n\nSIKE. I'm too high to even explode. Let's try again. 🤡")
    else:
        print(f"'{user_input}'? Bruh, my CPU is at 420 degrees, type 'yes' or 'no' before I melt.")

    print("\n[STALKER_V2.EXE IS STILL RUNNING]")
    print("-" * 40)
    time.sleep(1.5)