#Defining parent class
class student:
    def personal (self,name, age, gender):
        self.name= name
        self.age= age
        self.gender=gender
#First derived class "marks" inheriting properties from Parent class "Student"
class marks(student):
    def subjects (self, Physics, Chemistry, Maths, Biology):
        self.Physics= Physics
        self.Chemistry= Chemistry
        self.Maths= Maths
        self.Biology=Biology
#Inheriting from derived class "Marks"
class job(marks):
    def jobdetails (self,Position,Salary,Experience):
        self.Position= Position
        self.Salary=Salary
        self.Experience=Experience
##Defining derived class 3
class display(job):
    def information (self,name, age,gender,Physics,Chemistry, Maths, Biology, Position, Salary, Experience):
        student.personal(self, name, age, gender)
        marks.subjects(self,Physics, Chemistry, Maths, Biology)
        job.jobdetails(self,Position, Salary , Experience)
        print ('Name: {} \nAge: {} \nGender: {} \nPhysics: {} \nChemistry: {} \nMaths: {} \nBiology: {} \nPosition: {} \nSalary: {} \nExperience: {}'.format(self.name, self.age, self.gender,self.Physics,self.Chemistry,self.Maths,self.Biology,self.Position,self.Salary,self.Experience))
Biodata=display()
Biodata.information ('Shubham Gupta',20,'Male',40,50,60,70,'Python Developer',25000,10)

