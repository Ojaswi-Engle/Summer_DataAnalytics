'''Problem 15: Removal of all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510'''

s=input("enter  a string:")
result=''

for ch in s:
    if ch.isdigit():
        result+=ch
print(result)
