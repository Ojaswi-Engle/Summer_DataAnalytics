'''
Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user
'''

n=int(input("enter number of terms:"))
x=int(input("enter a number:"))

sum_=0
product=x

for i in range(1,n):
    product*=x
    term=product/(i+1)
    sum_+=term
sum_+=1
print("sum:",sum_)
