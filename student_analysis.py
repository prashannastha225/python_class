print("-" * 10 ,"Welcome to the student analysis!","-" * 10)

while True:

    Marks = float(input("State your total marks(1-100): "))

    if Marks >= 90.0 and Marks <= 100.0:
        print("A+, congrats!")

    elif Marks >= 80.0 and Marks < 90.0:
        print("A, You did great!")

    elif Marks >= 70.0 and Marks < 80.0:
        print("B+, You did good and you can do better!")

    elif Marks >= 60.0 and Marks < 70.0:
        print("B, You did well")

    elif Marks >= 50.0 and Marks < 60.0:
        print("C+, You can do better and please start to read more")

    elif Marks >= 40.0 and Marks < 50.0:
        print("C, You can do much better, stop focusing on games or the Internet too much")

    elif Marks < 40 and Marks >= 0:
        print("NG, Please read more, we expect much better from you")

    else:
        print("please give your marks accordng to the 1-100 figure")

    choice = input("Do you want to continue the program?(yes/no) ")

    if choice.lower() == "yes":
        continue

    elif choice.lower() != "yes":
        break

    else:
        print("error")
        break