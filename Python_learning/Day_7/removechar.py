# Write a program which can remove a particular character from a string.

s=input("enter a string:")
str=''
char=input("enter a character:")
while len(char)!=1:
    char=input("enter single character only :")

for ch in s:
    if ch!=char:
        str+=ch
print(str)
