# Write a python program to convert a string to title case without using the title()
s=input("enter a string:")
word=''
#logic 1
'''for i in range(len(s)):
    if i==0 and s[i]!=' ':
        word+=s[i].upper()
    elif s[i]!=' ' and s[i-1]==' ':
        word+=s[i].upper()
    else:
        word+=s[i]
print(word)'''
#logic2
'''inside=False
for ch in s:
    if ch!=' ' and inside==False:
        word+=ch.upper()
        inside=True
    elif ch==' ':
        inside=False
        word+=ch
    else:
        word+=ch
print(word)'''

#logic 3
'''for ch in s:
    if ch != ' ':
        word+=ch
    else:
        word=word[0].upper()+word[1::]
        print(word,end=' ')
        word=''
else:  
    word=word[0].upper()+word[1::]
    print(word,end=' ')'''

#logic 4
l=s.split()
for word in l:
    word=word[0].upper()+word[1::]
    print(word,end=' ')
        
