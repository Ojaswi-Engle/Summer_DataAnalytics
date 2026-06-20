"""Problem 4: Write a menu-driven program -
cm to ft
km to miles
USD to INR
exit"""

while True:

        menu = input("""ENTER choice for following conversions:
                1.enter 1 for cm -> ft
                2.enter 2 for km -> miles 
                3.enter 3 for USD-> INR
                4.enter 4 for exit\n""")
        if menu=='1':
            cm = float(input("enter value in cms :"))
            ft=0.0328*cm
            print(ft,"fts")
        elif menu=='2':
            km = float(input("enter value in kms :"))
            miles=km*0.621
            print(miles,"miles")
        elif menu=='3':
            USD= float(input("enter value in USD :"))
            INR=94.5*USD
            print(INR,"INR")
        elif menu=='4':
            print("EXIT")
            break
        else:
            print("INVALID input")
            

