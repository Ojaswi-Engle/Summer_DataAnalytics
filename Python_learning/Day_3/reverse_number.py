""" Problem 7 - Reverse a given integer number.
Example:

Input:

76542
Output:

24567

"""
n=int(input("enter a number:"))
rev=0
n1=n
while n != 0:
    last=n%10
    rev=rev*10+last
    n=n//10
print("reverse of ",n1," = ",rev)
