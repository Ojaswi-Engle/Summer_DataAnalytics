#the current population of a town is 10000.the population of the town is increasing at the rate of 10% per year. 
write a program to find out the population at the end of the last 10 years

current_population =10000
rate=0.1
prev_population=None

for i in range(10):
    prev_population=current_population/(rate+1)
    current_population =prev_population
    print("population of last ",i+1," year is ",int(prev_population))
