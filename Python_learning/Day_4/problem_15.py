"""Problem 15:Calculate the angle between the hour hand and minute hand.
Note: There can be two angles between hands; we need to print a minimum of two. 
Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.
Input:
H = 9 , M = 0
Output:
90
Explanation:
The minimum angle between hour and minute hand when the time is 9 is 90 degress.
"""
import math

H=int(input("enter hour:"))
M=int(input("enter minutes:"))

minute_hand=M*6
hour_hand=H*30+0.5*M

angle1=math.fabs(hour_hand-minute_hand)
angle2=360-angle1

print('angle between minute hand and hour hand :',min(math.floor(angle1),math.floor(angle2)))
