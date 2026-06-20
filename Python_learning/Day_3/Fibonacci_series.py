"""Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34"""



n = int(input("enter  number of terms :"))
a1=0
a2=1
if n<=0:
    print("invalid input")
elif n==1:
    print(a1)

else:
    print(a1,a2,end=" ")

    for i in range(n-2):
      an=a1+a2
      print(an,end=" ")
      a1=a2
      a2=an
