# Function to generate a list from 0 to the input number using a while loop
def number_sequence(n):
    sequence = []  # Initialize an empty list
    i = 0  # Start with 0
    while i <= n:  # Continue looping while i is less than or equal to n
        sequence.append(i)  # Append the current value of i to the list
        i += 1  # Increment i by 1 after each iteration
    return sequence

# Testing the function
print(number_sequence(5))  # Output: [0, 1, 2, 3, 4, 5]
