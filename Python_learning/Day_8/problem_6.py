#problem6  sum of natural logarithmic approximate series

n=int(input("enter number of terms:"))
x=int(input("enter a number:"))

sum_=0
term=((x-1)/x)
value=((x-1)/x)
for i in range(1,n):
    term*=value
    
    sum_+=term
sum_=value + (0.5 * sum_)
print("sum:",sum_)
