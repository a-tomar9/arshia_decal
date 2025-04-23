
import numpy as np

#1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    result = []
    for row in arr:
        if any(is_prime(num) for num in row):
            result.append(row)
    return np.array(result)

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
print(containsPrimes(arr))



#2.1
zeors_array = np.zeros( (8, 8) )
print(zeors_array)

#2.2
def create_matrix():
   
    matrix = np.zeros((8, 8), dtype=int) # Create a 8x8 matrix filled with zeros
    matrix[1::2, ::2] = 1 # Set the odd rows and even columns to 1
    return matrix

matrix = create_matrix()
print(matrix)

#2.3
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1  # Even rows, even columns
    board[1::2, 1::2] = 1  # Odd rows, odd columns
    return board

print(checkerboard())

#2.4
def reverse_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[1::2, ::2] = 1  # Odd rows, even columns
    board[::2, 1::2] = 1  # Even rows, odd columns
    return board

print(reverse_checkerboard())


#3
def expansion(arr, spaces):
    result = []
    for s in arr:
        expanded = (' ' * spaces).join(s)
        result.append(expanded)
    
    return np.array(result)

universe = np.array(['galaxy', 'clusters'])

print(expansion(universe, 1))

print(expansion(universe, 2))


#4
def secondDimmest(arr):
    sorted_arr = np.sort(arr, axis=0)
    return sorted_arr[1]

np.random.seed(123)  
stars = np.random.randint(500, 2000, (5, 5))  

print("Stars Array:")
print(stars)

result = secondDimmest(stars)

print("\nSecond Dimmest Stars (second smallest in each column):")
print(result)

