"""problem 14 Print all the Armstrong numbers in a given range.
Range will be provided by the user
Armstrong number is a number that is equal to the sum of cubes of its digits. 
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
"""

import math

l=int(input("enter lower range:"))
h=int(input("enter higher range:"))

i=l
while i<=h:
        if i==0:
            print(0,end=" ")
            i=i+1
            continue
        n1=n2=i
        sum=0
        count=0
        
        while n1!=0:
                n1=n1//10
                count+=1
        
        while n2!=0:
                d=n2%10
                sum+=int(math.pow(d,count))
                n2=n2//10
        
        if sum ==i:
                print(i,end=" ")
        i=i+1

