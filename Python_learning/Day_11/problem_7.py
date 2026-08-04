'''Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
Input:

['1ac21', '23fg', '456', '098d','1','kls']
Output:

['456', '23fg', '1ac21', '1', 'kls', '098d']
'''
#logic 1
l=['1ac21', '23fg', '456', '098d','1','kls']
p=[]

for s in l:
    prod=1
    present=False
    for ch in s:
        if ch.isdigit():
            prod*=int(ch)
            present=True
    if present:
        p.append(prod)
    else:
        p.append(1)

for k in range(len(p)-1):
    for m in range(len(p)-1-k):
        if p[m]<p[m+1]:
            p[m],p[m+1]=p[m+1],p[m]
            l[m],l[m+1]=l[m+1],l[m]
print(l)

#logic 2
l=['1ac21', '23fg', '456', '098d','1','kls']
p=[]

for s in l:
    prod=1
    present=False
    for ch in s:
        if ch.isdigit():
            prod*=int(ch)
            present=True
    if present:
        p.append(prod)

    else:
        p.append(1)

for k in range(len(p)-1):
    max=k
    for m in range(k+1,len(p)):
        if p[m]>p[max]:
            max=m
    p[k],p[max]=p[max],p[k]
    l[k],l[max]=l[max],l[k]
