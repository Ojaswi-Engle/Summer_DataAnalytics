'''Problem 13:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
Given:

str1 = PyNaTive

Expected Output:

yaivePNT'''

s=input("enter a string:")
lower=''
upper='' 
result=''

for ch in s:
    if ch.islower():
        lower+=ch
    if ch.isupper():
        upper+=ch
result=lower+upper
print(result)
