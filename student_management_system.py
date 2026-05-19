# Mini student management system(SMS)

student_details=[

#   {"id":1,"name":"ram","mark":[87,78,67,98,78]} --sutdent
#   {"id":1,"name":"ram",2}


]



student_details_list=set()

subjects=("Science","Math","English","Social","Nepali")

print("----------------Welcome to Mini Student Management System(SMS)-----------")

while True:
    print("Choose a number form 1 to 6\n")
    print("1.Add Student\n2.View Student\n3.Passed Student\n4.Failed Student\n5.Average\n6.Exit")
    
    choice=input("Enter your choice:")

    if choice<"1" or choice>"6":
        print("Invalid choice, Please enter the valid choice")
        continue

    match choice:
        case "1":
            # id=int(input("Enter the student id:"))
            # name=input("Enter the name of student:")
            # mark=float(input("Enter the mark of the student"))

            # studentadd={
            #     "id":id,
            #     "name":name,
            #     "mark":mark
            # }

            # student_details.append(studentadd)
            # print("Student added Successfully")

            id=int(input("Enter the student id:"))
            if id in student_details_list:
                print("Student id already exits")
                continue
            else:
                student_details_list.add(id)
                name=input("Enter the name of student:")
                mark_list=[]
                for i in subjects:
                    mark=float(input(f"Enter the mark for {i}:"))
                    mark_list.append(mark)

                
                studentadd={
                    "id":id,
                    "name":name,
                    "mark":mark_list
                }

                student_details.append(studentadd)
                print("Student Added Successfully")


        
        case "2":
            print("Id\tName\tMark")
            for i in student_details:
                print(f"{i['id']}\t{i['name']}\t{i['mark']}")

            

        case "3":
            # passed=0
            # for i in student_details:
            #     if i["mark"]>=40:
            #         print(i["name"])
            #         passed+=1  # passed =passed +1
            
            # print(f"The total no of passed students are:{passed}")

            for i in student_details:

                passed=0

                for j in i["mark"]:
                    if j>=40:
                        passed=passed+1
                    if passed==5:
                        print(i["name"])


        case "4":
            # failed=0
            # for i in student_details:
            #     if i["mark"]<40:
            #         print(i["name"])
            #         failed+=1  
            
            # print(f"The total no of failed students are:{failed}")

            totalstudent=0

            for i in student_details:

                failed=0

                for j in i["mark"]:
                    if j< 40:
                        failed=failed+1
                if failed>=1:
                    print(i["name"])
                    totalstudent=totalstudent+1
            
            print(f"The total failed students are:{totalstudent}")


        case "5":
            if not student_details:
                print("No data availiable")
            
            else:
                totalmarks=0
                totalsubject=0

                for i in student_details:
                    totalmarks=totalmarks+sum(i["mark"])
                    totalsubject=totalsubject+len(i["mark"])

                average=totalmarks/totalsubject
                print(f"Avg of studdent is:{average}")


        case "6":
            print("Exiting from the System")
            break