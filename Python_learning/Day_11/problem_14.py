'''
Problem 14: Write a list comprehension that can transpose a given matrix
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
'''
#logic 1
n=int(input("enter number of rows:"))
matrix=[]
for i in range(n):
    row=list(map(int,input("enter values:").split()))
    matrix.append(row)

transpose=[]

for i in range(len(matrix)):
    row=[]
    for j in range(len(matrix[i])):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)

#logic 2
n=int(input("enter number of rows:"))
matrix=[]
for i in range(n):
    row=list(map(int,input("enter values:").split()))
    matrix.append(row)

transpose=[ [  matrix[j][i]  for j in range(len(matrix[i]))] for i in range(len(matrix))]
print(transpose)

