from abc import ABC,abstractmethod

class shape(ABC) :
   @abstractmethod
   def area (self):
      pass

class circle (shape):
   def __init__(self,radius):
      self.radius = radius

   def area (self):
        return 3.14*self.radius**2

class triangle(shape):
   def __init__(self,base,height):
      self.base = base
      self.height = height 

   def area (self):
         return self.base * self.height * 0.5

class square (shape):
   def __init__(self,side):
     self.side = side 

   def area (self):
        return self.side**2

class pizza (circle):
   def __init__(self,topping,radius):
      super().__init__(radius)
      self.topping = topping

shapes = [circle(float(input ("Entre the radius of circle\n"))),triangle(float(input("Entre the base of triangle\n")),float(input("Entre the height of triange \n"))),square(float(input("Entre the side of square \n"))),pizza((input("Entre the toppings of pizza\n")),float(input("Entre the radius of pizza\n")))]

for shape in shapes:
   print (shape.area())
      