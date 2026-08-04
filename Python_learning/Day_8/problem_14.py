'''Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
Input:

hel123O4every093

Output:

Sum: 22
Avg: 2.75

'''
s=input("enter a string:")
total=0
average=0
count=0

for ch in s:
    
    if ch.isdigit():
        total+=int(ch)
        count+=1

if count==0:
    print('no digits present')
else:
    average=total/count
    print("sum = ",total)
    print("average = ",average)

