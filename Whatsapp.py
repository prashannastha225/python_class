import pyautogui as py
import time

print("Welcome to WhatsApp automation!")
time.sleep(2)
py.press("win")
time.sleep(1)
py.write("WhatsApp")
time.sleep(2)
py.press("enter")
time.sleep(2)
py.hotkey("ctrl","f")
time.sleep(2)
py.write("Python Batch -005D", interval=0.1)
time.sleep(5)
py.press("enter")

# To create a message

assignment = "Assignment: 1. write a small review about the python class"
py.write(assignment, interval=0.1)
time.sleep(2)
py.press("enter")
print("Whatsapp Automation completed succesfully!")