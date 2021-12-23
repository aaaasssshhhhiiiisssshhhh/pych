# #4. Write a Python program which accepts the radius of a circle from the user and compute the area.

# radius = float(input ("enter radius:"))

# area = (22/7)*radius *radius
# print(area)


#or 


from math import pi
r = float (input('enter radius:'))
print ("the area of the circle with radius:" +str(r)+ "is=" +str(pi * r**2))