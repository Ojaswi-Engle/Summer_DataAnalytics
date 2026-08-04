'''While working with Python tuples, we can have a problem in which we need to perform concatenation
 of records from the similarity of initial element. 
 This problem can have applications in data domains such as Data Science.

'''
#logic 1
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
result=[]
check=[]

for i in range(len(test_list)):
    if test_list[i][0] not in check:
        temp=set(test_list[i])
        check.append(test_list[i][0])

        for j in range(i+1,len(test_list)):
            if test_list[j][0]==test_list[i][0]:
                temp.update(test_list[j])
        result.append(tuple(sorted(temp)))

print(result)

#logic 2
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
result=[]
d={}

for (i,j) in test_list:
    if i not in d:
        d[i]=[]
    d[i].append(j)

for (i,j) in d.items():
    result.append((i,*j))

print(result)
