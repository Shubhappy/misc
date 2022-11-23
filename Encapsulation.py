#Program for encapsulation by accessing public variable and restricting private variable
#Defining class
class person:
    def personal(self,name,age,gender):     #Public variable
        self.name=name
        self.age=age
        self.gender=gender
        return self.name, self.age, self.gender
    
    def private(self,pan, aadhar, mobile):  #Private variable
        self._pan=pan
        self._aadhar=aadhar
        self.__mobile=mobile 
        return self._pan, self._aadhar, self.__mobile

print ("    Name    ", "Age", " Gender")
database=person()

print (database.personal("Shubham", "30", "male"))

database.private("BPAPG4567G",1234567890123456,"9876543210")

print("\nPAN no. ", database._pan)     #Weak private variable, variable is accessible
print("\nAadhar no. ", database._aadhar)  #Weak private variable, variable is accessible
print("")
print("Mobile no. ", database.__mobile) #not able to access private variable, throwing "AttributeError"
