'''
Problem 4:Write a program to print the following pattern
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

n=int(input("enter a number:"))

for i in range(1,n+1):
    a=i
    for j in range(1,i+1):
        print(a,end='')
        a-=1
    print()
