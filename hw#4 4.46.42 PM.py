#2.1
numbers = list(range(21))

print(numbers)  
"""i accidentally put numbers = range(21), the error: range() returns a range object, not a list."""


#2.2
def squareList(lst):
    return [x ** 2 for x in lst]

numbers = list(range(21))
squared_numbers = squareList(numbers)
print(squared_numbers)  


#2.3
def first_fifteen_elements(lst):
    return lst[:15]

print(first_fifteen_elements(squared_numbers))  # Output: [0, 1, 4, ..., 196]


#2.4
def every_fifth_element(lst):
    return lst[::5] 
"""i had put strided_list = my_list[::], the error: this slices the whole list, but could be misleading."""

print(every_fifth_element(squared_numbers)) 


#2.5
def fancy_function(lst):
    sliced_list = lst[-3:]  
    return sliced_list[::-3]  

print(fancy_function(squared_numbers))  


#3.1
def create_2d_list():
    matrix = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        matrix.append(row)
    return matrix

matrix = create_2d_list()
print(matrix)
"""i made an indentation error because the second loop was not properly indented."""

#3.2
def modified_2d_list(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = '?'
    return matrix

new_matrix = modified_2d_list(matrix)
print(new_matrix)
""" i got a syntaxerror, as `=` is used for assignment, not comparison. instead i woulf have to use `==` for comparison"""

#3.3
def sum_non_question_elements(matrix):
    total = 0
    for row in matrix:
        for element in row:
            if element != '?':
                total += element
    return total

result = sum_non_question_elements(new_matrix)
print(result)  # Output: 217
