'''
Problem 7 - Find the sum of the series upto n terms.
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.

Example 1:
Input:
5
Output:
2+22+222+2222+22222
Sum of above series is: 24690
'''
n=int(input("enter number of terms:"))

sum_=0
s=''
series=''
for i in range(n):
    s+='2'
    if i==0:
        series=s
    else:
        series+='+'+s

    sum_+=int(s)
print(series)
print('Sum of above series is:',sum_)
