'''Problem 9: Convert Character Matrix to single String using string comprehension.
Example 1:

Input:

[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
Output:

campux is best channel

'''
#logic 1
l=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
counter=len(l)
s=''

for i in l:
    for j in i:
        s+=j
    counter-=1
    if counter!=0:
        s+=' '
print(s)

#logic 2
l=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
result=[  ''.join(i)      for i in l]

print(' '.join(result))
