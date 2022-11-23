#Program for multiple inheritance
#Defining first super class
class father:
    def __init__ (self, eyes, height):
        self.eyes = eyes
        self.height = height
        print ("Son's eyes are as brown as father and height as high as father")
#Defining second super class
class mother:
    def __init__ (self, hair, color):
        self.hair = hair
        self.color = color
        print ("Son's hair is curly and color is fair as his mother")
#Defining first sub class
class child (father, mother):
    def __init__ (self, eyes, height, hair, color, daring, introvert):
        self.daring = daring
        self.introvert = introvert
        father.__init__(self, eyes, height)
        mother.__init__(self, hair, color)
        print ("The boy is very daring, but very shy in nature")
#creating object
Boy = child ('Brown', '6 feet', 'Black', 'Wheatish', 'Brave', 'Shy' )
Girl = child ('Blue', '5 feet', 'curly', 'Fair', 'Blunt', 'Shy' )
print (Boy.eyes)
print ("Boy child features are Eyes: {}, Height: {}, Hair: {}, Color: {}, Daring: {}, Introvert: {}".format (Boy.eyes, Boy.height, Boy.hair, Boy.color, Boy.daring, Boy.introvert))
print (Girl.daring)
print ("Girl Child features are Eyes: {}, Height: {}, Hair: {}, Color: {}, Daring: {}, Introvert: {}".format (Girl.eyes, Girl.height, Girl.hair, Girl.color, Girl.daring, Girl.introvert))