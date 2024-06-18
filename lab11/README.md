# Лабораторна робота №11: Розширене опрацювання масивів чисел у Python

## Мета роботи
Навчитися працювати з масивами чисел у Python, виконуючи різні операції, такі як обчислення сум, сортування за частотою, обертання масивів тощо.

## Опис завдання
Реалізувати функції для різних операцій з масивами чисел.


## Виконання роботи
### Кроки виконання
1. Створити папку для лабораторної роботи (наприклад, `lab11`).
2. Написати основний код програми у файлі `lab11.py`.
3. Створити README файл з детальним поясненням завдання і виконання.
4. Додати коментарі до коду для пояснення складних частин.
5. Завантажити роботу на GitHub.

### Структура проекту
# lab11/
# │
# ├── lab11.py
# └── README.md


### Опис файлів
- `lab11.py`: містить реалізацію функцій для виконання завдань з роботи з масивами чисел.
- `README.md`: документ з поясненням завдання, мети роботи, результатів та інструкцій з запуску.

### Опис основних функцій
#### Завдання 1: Сума квадратів
 Реалізувати функцію sum_of_squares, яка приймає масив чисел і повертає суму квадратів кожного числа.
```python
def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

# Приклад використання:
print(sum_of_squares([1, 2, 3]))  # Вивід: 14


```
### Завдання 2:  Фільтрація та сума
Реалізувати функцію filter_and_sum, яка приймає масив чисел і повертає суму всіх елементів, що більше або дорівнюють середньому значенню масиву.
```python
def filter_and_sum(numbers):
    average = sum(numbers) / len(numbers)
    return sum(x for x in numbers if x >= average)

# Приклад використання:
print(filter_and_sum([1, 2, 3, 4, 10]))  # Вивід: 14

```
### Завдання 3: Сортування за частотою
Реалізувати функцію `sort_by_frequency`, яка сортує масив чисел за частотою кожного елемента від найвищої до найнижчої. Якщо два числа мають однакову частоту, то менше число повинно бути першим.
```python
from collections import Counter

def sort_by_frequency(numbers):
    freq = Counter(numbers)
    return sorted(numbers, key=lambda x: (-freq[x], x))

# Приклад використання:
print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6]))  # Вивід: [4, 4, 4, 6, 6, 6, 2]


```
### Завдання 4: Знайти відсутнє число
Реалізувати функцію find_missing_number, яка знаходить відсутнє число в масиві, що містить всі цілі числа від 1 до n, крім одного.
```python
def find_missing_number(numbers):
    n = len(numbers) + 1
    return n * (n + 1) // 2 - sum(numbers)

# Приклад використання:
print(find_missing_number([1, 2, 4, 5]))  # Вивід: 3

```
### Завдання 5: Найдовша послідовність
Реалізувати функцію longest_consecutive, яка знаходить довжину найдовшої послідовності елементів у невідсортованому масиві.
```python
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

# Приклад використання:
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Вивід: 4


```
### Завдання 6: Обертання масиву
Реалізувати функцію rotate_array, яка обертає масив вправо на k кроків, де k не є від’ємним.
```python
def rotate_array(numbers, k):
    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k]

# Приклад використання:
print(rotate_array([1, 2, 3, 4, 5], 2))  # Вивід: [4, 5, 1, 2, 3]


```
### Завдання 7: Масив добутків
Реалізувати функцію `array_of_products`, яка обчислює масив добутків всіх чисел, крім поточного індексу, без використання ділення.
```python
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

# Приклад використання:
print(array_of_products([1, 2, 3, 4]))  # Вивід: [24, 12, 8, 6]

```
### Завдання 8: Максимальна сума підмасиву
Реалізувати функцію `max_subarray_sum`, яка знаходить максимальну суму неперервного підмасиву в одномірному масиві чисел.
```python
def max_subarray_sum(nums):
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Приклад використання:
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Вивід: 6

```
### Завдання 9: Спіральний порядок матриці
Реалізувати функцію spiral_order, яка повертає всі елементи двовимірної матриці в спіральному порядку.
```python
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

# Приклад використання:
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Вивід: [1, 2, 3, 6, 9, 8, 7, 4, 5]

```
### Завдання 10: k найближчих точок до початку координат
Реалізувати функцію k_closest_points, яка знаходить k найближчих точок до початку координат у двовимірному просторі, заданому масивом координатних точок.
```python
import math

def k_closest_points(points, k):
    distances = [(math.sqrt(x**2 + y**2), (x, y)) for x, y in points]
    distances.sort()

    return [point for _, point in distances[:k]]

# Приклад використання:
print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2))  # Вивід: [(1, 1), (1, 2)]

```

# Висновки
У цій лабораторній роботі ми детально розглянули різні аспекти роботи з масивами чисел у Python. Кожне завдання вимагало різних підходів до обробки даних:
1. Сума квадратів елементів масиву: Ми використали цикл для обрахунку квадратів кожного елемента та їх суми.
2. Фільтрування та сума: Реалізували функцію для фільтрування елементів, що перевищують середнє значення масиву, та обчислення суми цих елементів.
3. Сортування за частотою: Використали словник для підрахунку частоти кожного елемента, потім відсортували масив за частотою та значенням елементів.
4. Пошук відсутнього числа: Використали математичну формулу для знаходження відсутнього числа у відсортованому масиві чисел від 1 до n.
5. Найдовша послідовність чисел: Використали множини для ефективного пошуку найбільшої послідовності у несортованому масиві чисел.
6. Обертання масиву: Використали зрізи для обертання масиву на k позицій вправо.
7. Масив добутків: Використали два списки для зберігання лівих та правих добутків для кожного елемента, обчислили добутки для кожного елемента масиву.
8. Максимальна сума підрядного масиву: Використали алгоритм Кадане для пошуку максимальної суми з підрядного масиву чисел.
9. Спіральний порядок матриці: Реалізували алгоритм обходу матриці в спіральному порядку з використанням зовнішнього та внутрішнього циклів.
10. k найближчих точок до початку координат: Використали сортування за відстанню до початку координат для знаходження k найближчих точок у двовимірному просторі.








