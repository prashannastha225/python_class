print("-" * 15 + "number game" + "-" * 15)
a = int(input("give an integer: "))
b = int(input("give another integer: "))
c = int(input("give the last integer: "))

if a > b and a > c:
    print(f"The biggest number is {a}")
elif b > a and b > c:
    print(f"The biggest number is {b}")
else:
    print(f"The biggest number is {c}")