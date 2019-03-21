#'static'/class attributes
#these attributes/variables occupies a single storage location and
#are shared by all instances of the class
class Student():
    Studentcount = 0        #initialization outside any method is enough to make it static
    def __init__(self,name,roll):
        self.name = name
        self.rollno = roll
        Student.Studentcount +=1    #the static variables are refered by the class names
    def showdata(self):
        print('Name:',self.name)
        print('Roll No.:',self.rollno)

stud1 = Student('Jack',14)
stud2 = Student('Mark',9)
stud3 = Student('Toby',16)
stud4 = Student('Raj',20)
stud1.showdata()
stud4.showdata()
stud3.showdata()
print('stud2.Studentcount:',stud2.Studentcount)     #shows the same value
print('stud2.Studentcount:',stud4.Studentcount)     #as the variable is shared
print('Total no. of students:',Student.Studentcount)