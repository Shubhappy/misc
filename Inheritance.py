#Program for single level inheritance
#Super Class created
class human():
    def __init__(self, name,surname):
        self.name = name
        self.surname = surname

#sub class created
class identity (human):
    def First (self):
        return f"{self.name} is my first name"

    def Last (self):
        return f"{self.surname} is my last name"

    def fullname (self):
        return f"{self.name} {self.surname} is my full name"

#creating object using single level inheritance
naam = identity( "Shubham", "Gupta")

print (naam.First())
print (naam.Last())
print (naam.fullname())
