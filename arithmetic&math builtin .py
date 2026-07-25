f = 0
f +=1
f+=8
f*=3
f*=f
#reminder
f %=2
print (f)

x = 3.14
y= -4
z=5
result = round(x)#round up the value e.g = 4.8 = 5
result1=abs(y)#prints the absolute value of no.
result2 = pow(z,x)#The pow() function in Python is used to raise a number to a power (exponent) e.g print(pow(5, 2)) = 25
result3 = max(x,y,z)#shows the maximum value e.g shows the heighest value 
result4 = min(x,y,z)#shows the lowest value
print (result)
print (result1)
print(result2)
print (result3)
print (result4)

import math#can import maths functions 
print (math.pi)

x = 9
result5 = math.sqrt(x)
print (result5)

radius = float(input("entre the radius of a circle"))
circumference = 2*math.pi*radius
print (f"the circumference is : {round(circumference)}")
