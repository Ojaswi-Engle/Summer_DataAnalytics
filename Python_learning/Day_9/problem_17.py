'''Problem 17: Reverse words in a given String
Statement: We are given a string and we need to reverse words of a given string.'''

s=input("enter  a string:")

l=s.split()

for i in range(len(l)//2):
    temp=l[i]
    l[i]=l[len(l)-1-i]
    l[len(l)-1-i]=temp

s=' '.join(l)
print(s)
