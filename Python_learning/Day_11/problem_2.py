'''Problem 2: Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]'''

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

for i in list1:
    if type(i)==list:
        for j in i:
            if type(j)==list:
                pos=j.index(6000)
                j.insert(pos+1,7000)
print(list1)

#logic 2
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
inner=list1[2][2]
pos=inner.index(6000)
inner.insert(pos+1,7000)
print(list1)
