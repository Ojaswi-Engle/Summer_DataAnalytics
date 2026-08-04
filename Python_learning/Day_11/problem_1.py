'''Problem 1: Combine two lists index-wise(columns wise)
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

Given List:

list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
Output:

[['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]'''

#logic 1
list1=input().split()
list2=input().split()
result=[]

list1_=list1.copy()
list2_=list2.copy()

for i in range(min(len(list1_),len(list2_))):
    result.append([list1_[i],list2_[i]])
    list1.remove(list1_[i])
    list2.remove(list2_[i])

if list1!=[]:
    result.extend(list1)
elif list2!=[]:
    result.extend(list2)
print(result)

#logic 2
list1=input().split()
list2=input().split()
result=[]

for i in range(min(len(list1),len(list2))):
    result.append([list1[i],list2[i]])

temp=min(len(list1),len(list2))

if len(list1)>len(list2):
    result+=list1[temp:]
elif len(list2)>len(list1):
    result+=list2[temp:]
print(result)

#logic 3

result=[  [i,j]     for i,j in zip(list1,list2) ]

temp=min(len(list1),len(list2))

if len(list1)>len(list2):
    result+=list1[temp:]
elif len(list2)>len(list1):
    result+=list2[temp:]
print(result)


