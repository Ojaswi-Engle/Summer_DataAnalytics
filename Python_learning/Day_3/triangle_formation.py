""" 
Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
"""
angle1=int(input('enter first angle of triangle:'))
angle2=int(input('enter second angle of triangle:'))
angle3=int(input('enter third angle of triangle:'))

if angle1>0 and angle2>0 and angle3>0 and angle1+angle2+angle3 ==180:
    print("traingle can be formed")
else:
    print("traingle cannot be formed")

