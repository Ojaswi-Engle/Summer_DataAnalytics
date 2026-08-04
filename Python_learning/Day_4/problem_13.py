"""Problem 13:Write a program to print whether a given number is a prime number or not
"""
n=int(input("Enter a number:"))
if n<=1:
    print("neither prime nor composite")
else:
    prime_check=True
    for i in range(2,n):
        if n % i == 0:
            prime_check=False
            break

    if prime_check:
        print("prime")
    else:
        print("not prime")
