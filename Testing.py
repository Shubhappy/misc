"""
 Desc:
  Python program to demonstrate the diamond problem
  (a.k.a. Multiple Inheritance)
"""

'''# Parent class 1
class TeamMember(object):                   
   def __init__(self, name, uid): 
      self.name = name 
      self.uid = uid 
  
# Parent class 2
class Worker(object):                 
   def __init__(self, pay, jobtitle): 
      self.pay = pay 
      self.jobtitle = jobtitle 
  
# Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker):         
   def __init__(self, name, uid, pay, jobtitle, exp): 
      self.exp = exp 
      TeamMember.__init__(self, name, uid) 
      Worker.__init__(self, pay, jobtitle)
      print("Name: {}, Pay: {}, Exp: {}, jobtitle: {}".format(self.name, self.pay, self.exp, self.jobtitle))

TL = TeamLeader('Jake', 10001, 250000, 'Scrum Master', 5)'''

'''# Define a class as 'student'
class student:
    # Method
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")

# Define a class as 'test' and inherit base class 'student'
class test(student):
    # Method
    def getMarks(self):
        self.stuClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))

# Define a class as 'marks' and inherit derived class 'test'
class marks(test):
    # Method
    def display(self):
        print("\n\nName: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Study in: ",self.stuClass)
        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)


m1 = marks()
# Call base class method 'getStudent()'
m1.getStudent()
# Call first derived class method 'getMarks()'
m1.getMarks()
# Call second derived class method 'display()'
m1.display()'''

'''class shape:
    def area (self,side):
        print ("hello")
        self.side = side
        print (self.side*self.side)
 
sqr = shape()

sqr.area()'''

# import plotly.graph_objects as go
# Fruit=["Apples", "Oranges", "Bananas"]
# Contestant=["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"]
# Number_Eaten= [2, 1, 3]
# fig=go.Figure(go.Bar(x=Fruit[0:2], y=Number_Eaten[0:2]))
# fig.show()

# Importing required libraries

from plotly.graph_objs import Scatter, Figure, Layout
import plotly
import plotly.graph_objs as go
import json
import numpy as np
import geopandas as gpd

gdf = gpd.read_file('states_india.shp')
with open('states_india_1.json') as response:
    india = json.load(response)
fig = go.Figure(go.Choroplethmapbox(geojson=india, locations=gdf['st_nm'], z=gdf['state_code'],featureidkey="properties.st_nm",colorscale="Viridis", zmin=0, zmax=25,marker_opacity=0.5, marker_line_width=1))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3.5,mapbox_center = {"lat":23.537876 , "lon": 78.292142} ) 
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()