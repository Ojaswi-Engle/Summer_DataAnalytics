'''Problem 8: Split String of list on K character.

Example :

Input:

['CampusX is a channel', 'for data-science', 'aspirants.']
Output:

['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
'''
'''Problem 8: Split String of list on K character.

Example :

Input:

['CampusX is a channel', 'for data-science', 'aspirants.']
Output:

['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
'''
#logic 1

l=['CampusX is a channel', 'for data-science', 'aspirants.']
result=[]

for string in l:
    word=''
    for ch in string:
        if ch!=' ':
            word+=ch
        else:
            if word!='':
                result.append(word)
                word=''
    if word!='':
        result.append(word)

print(result)

#logic 2
l=['CampusX is a channel', 'for data-science', 'aspirants.']
s=' '.join(l)
l=s.split()
print(l)  
