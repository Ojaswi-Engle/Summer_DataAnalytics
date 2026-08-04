"""Problem 11: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
each digit of the number is an even number. 
The numbers obtained should be printed in a space-separated sequence on a single line.
"""
i=1000
while i<=3000:
    n=i
    check=True
    while n!=0:
        d=n%10
        if d%2!=0:
            check=False
            break
        n=n//10
    if check:
        print(i,end=" ")
    i=i+1
