'''Problem 6: Find list of common unique items from two list. and show in increasing order
Input

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
Output:

[34, 67, 89]

'''

num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
result=[]

for i in num1:
    if i in  num2 and i not in result:
        result.append(i)

print(sorted(result))
