import math
class Circle():
    def __init__(self,r):
        self.radius = r
    
    def getArea(self):
        area = math.pi * math.pow(self.radius,  2)
        print("Area of circle: ",area)
    
    def getCircumference(self):
        circum_fere = 2* math.pi * self.radius
        print("The Circumference of the circle is: ", circum_fere)

    def getArea22(self):
        print("3.14*self.radius*self.radius")
c1 = Circle(7)
c1.getArea()
c1.getCircumference()

