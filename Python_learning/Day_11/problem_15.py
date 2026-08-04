'''Problem 15: Write a list comprehension that can flatten a nested list
Input
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

l=[]
n=int(input("enter number of  rows:"))
for i in range(n):
    row=list(map(int,input("enter values:").split()))
    l.append(row)
result=[]
for j in l:
    for k in j:
        result.append(k)
print(result)

#logic 2
result=[   j        for i in l    for j in i]
print(result)
