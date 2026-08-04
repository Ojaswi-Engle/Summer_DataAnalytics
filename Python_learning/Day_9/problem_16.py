'''Check whether the string is Symmetrical.
Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

Example 1:

Input

khokho
Output

The entered string is symmetrical'''

#logic 1
s=input("enter a string:")

'''if len(s) % 2==0:
    for i in range(len(s)//2):
        if s[i] != s[i+len(s)//2]:
            print('the entered string is unsymmetrical')
            break

    else:
        print('the entered string is symmetrical')
else:
    print('entered string is unsymmetrical')'''
#logic 2


if len(s) % 2==0:
    s1=s[0:len(s)//2]
    s2=s[len(s)//2:]
    if s1==s2:
            print('the entered string is symmetrical')
            

    else:
        print('the entered string is unsymmetrical')
else:
    print('entered string is unsymmetrical')

