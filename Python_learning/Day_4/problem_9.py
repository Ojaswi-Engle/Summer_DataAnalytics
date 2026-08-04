""""Problem 9: Write a program that keeps on accepting a number from 
the user until the user enters Zero.
Display the sum and average of all the numbers.
"""


sum=0
avg=0
counter=0

while True:
    n=int(input("Enter a number:"))

    if n==0:
        break
    sum=sum+n
    counter=counter+1
if counter==0:
    print("no number entered")
else:
    avg=sum/counter
    print('\nsum of all numbers:',sum)
    print('\navg of all numbers:',avg)
