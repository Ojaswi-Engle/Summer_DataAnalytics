'''Problem 20: Write a program that can remove all the duplicate characters from a string. 
User will provide the input.'''

s=input("enter a string:")
result='' 

for ch in s:
    if ch not in result:
        result+=ch

print(result)
