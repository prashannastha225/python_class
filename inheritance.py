class User:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Hi! I am from User, Hello! {self.name} and my id is {id}")

class Student(User):

    def __init__(self,name,mark):
        User.__init__(self,name,id)     # we initialize the parent constructor here
        self.mark = mark

    def fromstudent(self):
        print(f"I am from student, hi {self.name}") # child class can access the properties of parent class

student_1 = Student("ram","stu1")
student_1.show()
print(student_1.mark)

student_1.fromstudent()