#1
x = 2
y = 3
import math
print(math.pow(x,y))

#2
reading = [15, 14, 17, 20,23, 28, 20]
def temperaturerange(reading):
    return(min(reading), max(reading))
print(temperaturerange(reading))

#3
def isweekend(day):
    '''saturday = 6, sunday = 7'''
    if day == 6:
     return True
    if day == 7:
       return True
    else:
       return False
print(isweekend(6))

#4
distance = 70 
fuel = 21.5
def fuelefficiency(distance,fuel):
   return round(distance/fuel, 2)
print(fuelefficiency(distance, fuel))

#5
def decodenumbers(n):
   last_digit = n%10
   remaining_number = n//10

   num_digits = 0
   temp = remaining_number
   while temp > 0:
      num_digits += 1
      temp //= 10

   new_number = last_digit * (10 ** num_digits) + remaining_number
    
   return new_number

n=12345
print(decodenumbers(n))

#COMEBACKTOTHIS 

#6.1
# def find_min_with_for_loop(nums):
#    find_


#7
