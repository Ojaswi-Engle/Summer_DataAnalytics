"""
Problem 16:Given two rectangles, find if the given two rectangles overlap or not. 
A rectangle is denoted by providing the x and y coordinates of two points: 
the left top corner and the right bottom corner of the rectangle. 
Two rectangles sharing a side are considered overlapping. 
(L1 and R1 are the extreme points of the first rectangle and L2 
and R2 are the extreme points of the second rectangle).
"""
L1_x=int(input("enter x coordinate of left top corner  of first rectangle : "))
L1_y=int(input("enter y coordinate of left top corner  of first rectangle : "))

R1_x=int(input("enter x coordinate of right bottom corner  of first rectangle : "))
R1_y=int(input("enter y coordinate of right bottom corner  of first rectangle : "))

L2_x=int(input("enter x coordinate of left top corner  of second rectangle : "))
L2_y=int(input("enter y coordinate of left top corner  of second rectangle : "))

R2_x=int(input("enter x coordinate of right bottom corner  of second rectangle : "))
R2_y=int(input("enter y coordinate of right bottom corner  of second rectangle : "))

if R1_x < L2_x or R2_y > L1_y or R2_x < L1_x or L2_y < R1_y:
    print(" both rectangles do not overlap each other")
else:
    print(" both rectangles overlap each other")
    



