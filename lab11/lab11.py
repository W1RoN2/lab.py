#Task 1
def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

#Task 2
def filter_and_sum(numbers):
    average = sum(numbers) / len(numbers)
    return sum(x for x in numbers if x >= average)

from collections import Counter

#Task 3
def sort_by_frequency(numbers):
    freq = Counter(numbers)
    return sorted(numbers, key=lambda x: (-freq[x], x))

#Task 4
def find_missing_number(numbers):
    n = len(numbers) + 1
    return n * (n + 1) // 2 - sum(numbers)

#Task 5
def longest_consecutive(numbers):
    numbers_set = set(numbers)
    longest_streak = 0

    for number in numbers:
        if number - 1 not in numbers_set:
            current_number = number
            current_streak = 1

            while current_number + 1 in numbers_set:
                current_number += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

#Task 6
def rotate_array(numbers, k):
    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k]

#Task 7
def array_of_products(numbers):
    length = len(numbers)
    left_products = [1] * length
    right_products = [1] * length
    products = [1] * length

    for i in range(1, length):
        left_products[i] = left_products[i - 1] * numbers[i - 1]

    for i in range(length - 2, -1, -1):
        right_products[i] = right_products[i + 1] * numbers[i + 1]

    for i in range(length):
        products[i] = left_products[i] * right_products[i]

    return products

#Task 8
def max_subarray_sum(numbers):
    max_sum = current_sum = numbers[0]

    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)

    return max_sum

#Task 9
def spiral_order(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

import math

#Task 10
def k_closest_points(points, k):
    distances = [(math.sqrt(x**2 + y**2), (x, y)) for x, y in points]
    distances.sort()

    return [point for _, point in distances[:k]]
