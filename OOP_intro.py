"""

Characteristics of OOP:
(i) inheritance
(ii) polymorphism
(iii) encapsulation
(iv) abstraction
(v) reusability
(vi) message passing

"""
#OOP means object oriented programming
# class Show:
#     name = "ram"

#     def show_details(self):
#         print("Hello! I am from show_details")

# stu = Show()
# print(stu.name)
# print(stu.show_details())



# class Student:

#     name = "hari"
#     age = 78

#     def __init__(self,name):
#         self.name = "krishna"
#         self.age = "23"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print("I am from show method")

# stu1 = Student("ram", "23")
# stu2 = Student("shyam", "88")

# stu1 = Student()
# print(stu1.name)

# stu2 = Student("shyam","88")
# print(stu2.name)

# stu3 = Student("ganesh","45")
# print(stu3.name)

# print(stu1.show())


class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm from show method hi, {self.name}")


stu1 = student("ram","26")
print(stu1.name)

stu1 = "shiva"

stu1.contact = "9845878654"
print("\n")
print(stu1.contact)
print("\n")