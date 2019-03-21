#Attribute Methods
#bulit-in methods to add/modify/delete attributes of instances
class Student():
    Stdcount = 0
    def __init__(self,roll,name):
        self.name = name
        self.rollno = roll
        Student.Stdcount += 1
    def showData(self):
        print('Name:',self.name)
        print('Roll No.:',self.rollno)

stud1 = Student(102,'Jack')
stud1.showData()
print('getattr(stud1,\'name\'):',getattr(stud1,'name')) #shows the value of the attribute given
print('hasattr(stud1,\'rollno\'):',hasattr(stud1,'rollno')) #shows whether the object has the given attribute
print('setattr(stud1,\'rollno\',105):',setattr(stud1,'rollno',105))  #sets the value of the given attribute of the object
stud1.showData()
print('delattr(stud1,\'rollno\'):',delattr(stud1,'rollno'))  #deletes a given attribute of the object
print('delattr(Student,\'Stdcount\'):',delattr(Student,'Stdcount')) #deletes a given attribute of the class
print('hasattr(Student,\'Stdcount\'):',hasattr(Student,'Stdcount'))
print('stud1.__dict__:',stud1.__dict__)