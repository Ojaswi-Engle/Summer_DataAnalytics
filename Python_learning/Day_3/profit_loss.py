"""Problem 3: Write a program that will take user input of cost price and selling price 
and determines whether its a loss or a profit."""

cost_price=float(input("enter cost price(in rupees) :"))
selling_price=float(input("enter selling price(in rupees) :"))

if cost_price>selling_price:
    print("LOSS : ",cost_price-selling_price)
elif cost_price<selling_price:
    print("PROFIT : ",selling_price-cost_price)
else:
    print("NEITHER PROFIT NOR LOSS ")
