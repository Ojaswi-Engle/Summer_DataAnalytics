# Write a program to count the number of words in a string without split()

s=input("enter a string:")
count=0
#logic 1
'''for i in range(len(s)):
    if i==0 and s[i]!=' ':
        count+=1
    elif s[i]!=' ' and s[i-1]==' ':
        count+=1
print("words:",count)'''
#logic 2
'''inside=False
for ch in s:
    if ch!=' ' and inside==False:
        count+=1
        inside=True

    elif ch==' ':
        inside=False


print("words:",count)'''

#logic 3
word=''
l=[]
for ch in s:
    if ch!=' ':
        word+=ch
    else:
        l.append(word)
        word=''
l.append(word)
print("words:",len(l))

