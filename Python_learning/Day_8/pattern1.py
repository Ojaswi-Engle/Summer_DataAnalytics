'''Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''

n=int(input("enter a number:"))

for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end='')
    print()
