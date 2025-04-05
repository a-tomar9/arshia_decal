#1
def computePower(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result
x = 2
y = 3
print(computePower(x, y)) 


#2
def temperatureRange(readings):
    return (min(readings), max(readings))

readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings))  


#3
def isWeekend(day):
    return day == 6 or day == 7

day = 6  
print(isWeekend(day)) 


#4
def fuel_efficiency(distance, fuel):
    return distance / fuel

distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))  

#5
def decodeNumbers(n):
    last_digit = n % 10
    remaining_number = n // 10
    num_digits = len(str(n)) - 1
    return last_digit * (10 ** num_digits) + remaining_number

n = 12345
print(decodeNumbers(n))  

#6.1
def find_min_with_for_loop(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value

def find_max_with_for_loops(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums)) 
print(find_max_with_for_loops(nums))  

#6.2
def find_min_with_while_loop(nums):
    min_value = nums[0]
    index = 1
    while index < len(nums):
        if nums[index] < min_value:
            min_value = nums[index]
        index += 1
    return min_value

def find_max_with_while_loops(nums):
    max_value = nums[0]
    index = 1
    while index < len(nums):
        if nums[index] > max_value:
            max_value = nums[index]
        index += 1
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_while_loop(nums))  
print(find_max_with_while_loops(nums))  


#7
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))  

#8
def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

num = 2468
print(digital_root(num)) 





