'''
problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers
'''
#logic 1
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
a=n1
b=n2

'''for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        hcf=i

lowest=max(n1,n2)

while True:
    if lowest % n1==0 and lowest % n2==0:
        lcm=lowest
        break
    lowest+=1
print("hcf",hcf)
print('lcm',lcm)'''
#logic 2
'''l1=[]
l2=[]
common=[]
i=2
j=2

while n1!=1:
    if n1 % i==0:
        n1=n1//i
        l1.append(i)
    else:
        i+=1
while n2!=1:
    if n2 % j==0:
        n2=n2//j
        l2.append(j)
    else:
        j+=1
l1_=l1.copy()
for k in l1:
    if k in l2:
        common.append(k)
        l1_.remove(k)
        l2.remove(k)

prod=1
for l in common:
    prod*=l

lcm=prod
for m in l1_:
    lcm*=m

for n in l2:
    lcm*=n
print("hcf",prod)
print('lcm',lcm)'''

#logic 3 euclidean algo
while n2!=0:
    r=n1%n2
    n1=n2
    n2=r
hcf=n1
lcm=a*b//hcf
print("hcf",hcf)
print('lcm',lcm)


