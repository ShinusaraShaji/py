class student:
    def __init__(self,rollnumber,name,course):
        self.rollnumber=rollnumber
        self.name=name
        self.course=course
    def displaystudent(self):
            print("RollNumber is:",self.rollnumber)
            print("name:",self.name)
            print("course:",self.course)
stud1=student(10,"Jack","MCA")
stud2=student(20,"james","MCA")
stud1.displaystudent()
stud2.displaystudent()

    
