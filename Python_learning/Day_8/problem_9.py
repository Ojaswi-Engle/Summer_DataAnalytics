'''
Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number

'''

deci=int(input("enter decimal number:"))
bin=0
a=1

while deci!=0:
    r=deci%2
    bin+=r*a
    a*=10
    deci//=2
print(bin)
