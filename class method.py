class student :
    total_student = 0
    total_gpa = 0 

    def __init__ (self,name,gpa):
        self.name = name 
        self.gpa = gpa
        student.total_student +=1
        student.total_gpa += gpa

    def get_info (self):
        return f"{self.name}{self.gpa}"

    @classmethod
    def get_total_students (cls):
        return f"Total no. of student is {cls.total_student}"

    @classmethod
    def get_average_gpa (cls):
        if cls.total_student == 0 :
            return 0
        else :
          avg = cls.total_gpa / cls.total_student
          return f"Average gpa of students is {avg}"

student1 = student("aryan",98)
student2 = student("aryan",99)
student3 = student("kaku",89)

print (student1.get_info())
print (student2.get_info())
print (student3.get_info())
print (student.get_total_students())
print (student.get_average_gpa())