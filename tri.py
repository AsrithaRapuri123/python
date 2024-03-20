'''Design a function that should check the sides entered are valid or not.? 
If the sides of a triangle are valid, Then It should print the message to enter the angles. 
(Since the Sum of Angles in a triangle should be 180 Degrees). 
If the angles are also valid, Print a message that it is a valid triangle.'''


def triangle():
    a=int(input("enter side1:"))
    b=int(input("enter side1:"))
    c=int(input("enter side1:"))
            
    if a+b>=c and b+c>=a and a+c>=b:
       print("sides are valid")

       x=int(input("enter angle1:"))
       y=int(input("enter angle2:"))
       z=int(input("enter angle3:"))

            
       if x+y+z==180:
             print("valid triangle")
       else:
              print("angles are not valid")
    else:
       print("sides are not valid")
triangle() 