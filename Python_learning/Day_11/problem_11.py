'''Problem 11:  Write a program that can perform union operation on 2 lists
Example:

Input:

[1,2,3,4,5,1]
[2,3,5,7,8]
Output:

[1,2,3,4,5,7,8]'''

list1=list(map (int,input().split()))
list2=list(map (int,input().split()))
result=[]
total=list1+list2

for i in total:
    if i not in result:
        result.append(i)

print(sorted(result))
