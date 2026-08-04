'''
Problem 11: Create Short Form from initial character
Given a string create short form ofthe string from Initial character. Short form should be capitalised.

Example:

Input:

Data science mentorship program
Output:

DSMP
'''

s=input("enter a string:")
shortform=''

s=s.title()
l=s.split()

for word in l:
    shortform+=word[0]

print("shortform : ",shortform)
