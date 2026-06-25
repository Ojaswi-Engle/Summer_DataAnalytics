#wap to convert integer to string 
i=int(input("enter an integer:"))
s=''
digits='0123456789'
while i != 0:
    s=digits[i % 10]+s
    i=i//10
print(s)
