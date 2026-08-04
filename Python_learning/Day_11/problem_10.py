'''Problem 10: Add Space between Potential Words.
Example:

Input:

['campusxIs', 'bestFor', 'dataScientist']
Output:

['campusx Is', 'best For', 'data Scientist']

'''
#logic 1

l=input().split()
result=[]

for s in l:
    word=''
    index=0
    for ch in s:
        if index==0 and ch.isupper():
            word+=ch
        elif ch.isupper():
            word=word+' '+ch
        else:
            word+=ch
        index+=1
    result.append(word)
print(result)

#logic 2
l=input().split()
for i in range(len(l)):
    word=''
    index=0
    for ch in l[i]:
        if index==0 and ch.isupper():
            word+=ch
        elif ch.isupper():
            word=word+' '+ch
        else:
            word+=ch
        index+=1
    l[i]=word
print(l)
#logic 3
l=input().split()
result=[]
for s in  l:
    l_=list(s)
    shift=0
    for i in range(len(s)):
        if i!=0 and s[i].isupper():
            l_.insert(i+shift,' ')
            shift+=1
    result.append(''.join(l_))
print(result)

#logic 4
l=input().split()
result=[]
for s in  l:
    l_=list(s)
    shift=0
    for i in range(len(s)):
        if i!=0 and l_[i+shift].isupper():
            l_.insert(i+shift,' ')
            shift+=1
    result.append(''.join(l_))
print(result)



