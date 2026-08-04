'''Problem 12: Append second string in the middle of first string
Input:

campusx
data
Output:

camdatapusx'''
#logic1
first=input("enter first string:")
second=input("enter second string:")
result=''
'''result=first[0:len(first)//2]+second+first[len(first)//2:]
print(result)'''

#logic 2

for i in range(len(first)):
    result+=first[i]

    if i==(len(first)//2)-1:
        result+=second
print(result)


