import sys
import time
import math

def print_slow(text):
    """Prints text character-by-character for a retro feel"""
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.03)
    print()

# 1. Get the math data
theta_deg = float(input("Enter theta (angle in degrees): "))
hyp = float(input("Enter hypotenuse length: "))

# 2. Do the math
theta_rad = math.radians(theta_deg)
opp = math.sin(theta_rad) * hyp
adj = math.cos(theta_rad) * hyp

# 3. The "Email Style" report block
# The 'f' before the quotes lets us put {variables} inside
report = f"""
>>> TRIANGLE CALCULATION COMPLETE <<<
------------------------------------
INPUT DATA:
  Angle (θ):   {theta_deg}°
  Hypotenuse:  {hyp}

GEOMETRY RESULTS:
  Height (Opp): {opp:.4f}
  Width (Adj):  {adj:.4f}

SYSTEM STATUS: 
  Calculation successful.
------------------------------------
"""

# 4. Print it slow!
print_slow(report)