""" Problem 12: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
The numbers after the direction are steps.

! means robot stop there.

Please write a program to compute the distance from current position after a sequence of movement and original point.

If the distance is a float, then just print the nearest integer.

Example:

Input:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
Output:

2

"""



current_x=0
current_y=0
original_x=0
original_y=0
while True:
    direction=input() 
    if direction=="!":
        break
    steps=int(input())
    if direction=="UP":
        
        current_y+=steps
        
    elif direction=="DOWN":
        
        current_y-=steps
    elif direction=="LEFT":
       
        current_x-=steps
    elif direction=="RIGHT":
        
        current_x+=steps
    
    

dist=round(((current_x-original_x)**2+(current_y-original_y)**2)**0.5)
print("Distance between (0,0) and (",current_x,",",current_y,") = ",dist)
