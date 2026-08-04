'''Write a program that can find the max number of each row of a matrix
Example:

Input:

[[1,2,3],[4,5,6],[7,8,9]]
Output:

[3,6,9]

'''
#logic 1
matrix=[]
result=[]
n=int(input("enter number of rows:"))
for i in range(n):
    row=list( map(int,input("enter values:").split()))
    matrix.append(row)

for i in matrix:
    max_value=i[0]
    for j in range(1,len(i)):
        if i[j]>max_value:
            max_value=i[j]
    result.append(max_value)

print(result)

#logic 2
matrix=[]

n=int(input("enter number of rows:"))
for i in range(n):
    row=list( map(int,input("enter values of : ").split()))
    matrix.append(row)


result=[ max(i)     for i in matrix]
print(result)
