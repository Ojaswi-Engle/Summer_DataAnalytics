"""Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
above 20 : 30% 
"""

CTC = float(input("enter salary in lakhs(per year):"))

HRA=0.1*CTC
DA=0.05*CTC
PF=0.03*CTC
if CTC < 5:
    tax=0
elif CTC<=10:
    tax=0.1*CTC
elif CTC<=20:
    tax=0.2*CTC
else:
    tax=0.3*CTC
salary=(CTC-HRA-DA-PF-tax)
in_handmonthlysalary=(salary/12)*100000
print("In hand monthly salary :",in_handmonthlysalary)

