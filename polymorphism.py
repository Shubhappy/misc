
#Program for polymorphism
#Author: Shubham Gupta
shape_type=input("Enter the shape name for area calculation: ")
shape=shape_type.upper()
#shapes taken for program are "SQUARE","TRIANGLE","CIRCLE","RECTANGLE","TRAPEZOID"

class square:
    def area (self):
        side=int(input("Please enter the side: "))
        self.side=side
        print ("Area of Square :", self.side*self.side)

class Triangle:
    def area (self):
        base= int(input("Please enter the base: "))
        height= int(input("Please enter the height: "))
        self.base=base
        self.height=height
        print (0.5*self.base*self.height)

class circle:
    def area (self):
        radius = int (input ("Enter the radius: "))
        self.radius=radius
        print (3.14*self.radius*self.radius)

class rectangle:
    def area (self):
        length = int (input ("Enter the length: "))
        width = int (input ("Enter the width: "))
        self.length=length
        self.width=width
        print (self.length*self.width)

class Trapezoid:
    def area (self):
        side1 = int (input ("Enter the side1: "))
        side2 = int (input ("Enter the side2: "))
        height = int (input ("Enter the height: "))
        self.side1=side1
        self.side2=side2
        self.height=height
        print (0.5*(self.side1+self.side2)*self.height)
        

sqr = square()
tri=Triangle()
cir=circle()    
rect=rectangle()
trap=Trapezoid()

if shape=="SQUARE":
    sqr.area()
elif shape=="TRIANGLE":
    tri.area()
elif shape=="CIRCLE":
    cir.area()
elif shape=="RECTANGLE":
    rect.area()
elif shape=="TRAPEZOID":
    trap.area()
else:    
    print("Error in name of shape, please type correctly")