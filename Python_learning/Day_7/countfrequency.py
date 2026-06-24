# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

s=input("enter a string:")
freq=0
char=input("enter a character:")

while len(char)!=1:
    char=input("enter a single character again:")

else:
    for ch in s:
        if ch==char:
            freq+=1
    print("frequency : ",freq)
