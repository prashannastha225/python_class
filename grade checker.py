print("------------------Welcome to Grade Checker----------------")

while True:

    marks=float(input("Enter your mark"))

    if marks>=90 and marks<=100:
        print("A+")

    elif marks>=80 and marks<90:
        print("A")

    elif marks>=70 and marks<80:
        print("B+")

    elif marks>=60 and marks<70:
        print("B")

    elif marks>=50 and marks<60:
        print("C+")

    elif marks>=40 and marks<50:
        print("C")
    elif marks>=35 and marks<40:
        print("D grade")
    else:
        print("NG")
    
    choice=input("Do you want to continue(Yes/No)")
    if choice=="Yes":
        continue
        print("This wont run, when we use continue, this will take back to while loop for next iteration without running the code after continue")
       
    else:
        print("Thank you for using grade checker")
        break