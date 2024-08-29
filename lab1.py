import math
A=math.pi*5**2
print("Circle of radius 5", A)
V=4/3*math.pi*5**3
print("circle of radius 3" , V)
B=3**2
C=4**2
D=B+C
print("Triangle area of base 3, height 4 iw" , D)

fullname=("Charle Andrew Hahn")
print('length of full name:', len(fullname), 'characters')
uppercasename=fullname.upper()
print('Full name in uppercase', uppercasename)

age=38
height=70
weight=260

aget=type(age)
print("My age is ", age, " years old")
print("Age variable is of type: ", aget)
heightt=type(height)
print ("My height is ", height, " inches")
print("Height variable is of type: ", heightt)
print("My weight is ", weight)
print("Weight variable is of type: ", type(weight))

BMI=weight/(height**2)*703
print("My BMI is ", BMI)


