'''Problem 13: Write a list comprehension to print the following matrix
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]


[ ]
'''

#logic 1
matrix=[]
a=0
for i in range(3):
    row=[]
    for j in range(3):
        row .append(a)
        a+=1
    matrix.append(row)
print(matrix)

#logic 2
result=[ [ i*3+j       for j in range(3)]    for i in range(3)]
print(result)
