import random

def task1(a, b, c):
    return max(a, b, c)

def task2(numbers):
    return sum(numbers)

def task3(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def task4(string):
    return string[::-1]

def task5(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def task6(number):
    return 25 <= number <= 50

def task7(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

def task8(lst):
    return list(set(lst))

def task9(lst):
    return [num for num in lst if num % 2 == 0]

def task10():
    def generate_pascals_triangle(num_rows):
        triangle = []
        for row_num in range(num_rows):
            row = [1] * (row_num + 1)
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
    
    num_rows = 10  # Кількість рядків трикутника Паскаля
    pascals_triangle = generate_pascals_triangle(num_rows)
    last_row = pascals_triangle[-1]
    max_number = max(last_row)
    
    return max_number

