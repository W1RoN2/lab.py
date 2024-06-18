# Лабораторна робота №3: Рядки, оператори, цикли

## Мета роботи
Ознайомитися з використанням рядків, операторів та циклів у мові програмування Python. Навчитися виконувати основні операції зі списками та рядками, використовуючи різні типи циклів.

## Опис завдання
1. Використовувати оператори та цикли для виконання завдань зі списками та рядками.
2. Реалізувати функції для різних завдань, описаних нижче.

## Виконання роботи
### Кроки виконання
1. Створити папку для лабораторної роботи (наприклад, `lab3`).
2. Написати основний код програми у файлі `main.py`.
3. Створити README файл з детальним поясненням завдання і виконання.
4. Додати коментарі до коду для пояснення складних частин.
5. Завантажити роботу на GitHub.

### Структура проекту
# lab3/
# │
# ├── lab3.py
# └── README.md

### Опис файлів
- `lab3.py`: містить реалізацію функцій для виконання завдань.
- `README.md`: документ з поясненням завдання, мети роботи, результатів та інструкцій з запуску.

### Опис основних функцій
#### Завдання 1
Функція `task1` приймає значення `my_list`. Додає число -5 на другу позицію у списку, знаходить мінімальний та максимальний елементи списку, додає список [1, 2, 3] на третю позицію, додає елемент з прізвищем та ім'ям наприкінці списку, визначає довжину списку. Повертає значення `my_list`, `min_element`, `max_element`, `list_length`.

```python
def task1(my_list):
    my_list.insert(1, -5)
    min_element = min(my_list)
    max_element = max(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append(["Прізвище", "Ім'я"])
    list_length = len(my_list)
    print(my_list)
    print(min_element)
    print(max_element)
    print(list_length)
    return my_list, min_element, max_element, list_length

# Приклад використання
my_list = [10, 20, 30]
result = task1(my_list)
print(result)
# Вивід: ([10, -5, [1, 2, 3], 20, 30, ['Прізвище', "Ім'я"]], -5, 30, 6)
```
### Завдання 2
Функція task2 приймає три списки A, B та C. Обчислює загальну вартість товарів на складі, середню ціну товарів та знаходить товар з найбільшою кількістю одиниць. Повертає значення total_cost, average_price, most_stocked_item.
```python
def task2(A, B, C):
    total_cost = sum([B[i] * C[i] for i in range(len(A))])
    average_price = sum(C) / len(C)
    most_stocked_item = A[B.index(max(B))]
    return total_cost, average_price, most_stocked_item

# Приклад використання
A = ["item1", "item2", "item3"]
B = [10, 20, 30]
C = [5, 10, 15]
result = task2(A, B, C)
print(result)
# Вивід: (650, 10.0, 'item3')
```
### Завдання 3
Функція task3 формує список із 50 елементів в діапазоні від -25 до 25, розподіляє додатні елементи у список A1, від’ємні в A2. Повертає значення A1 та A2.
```python
import random

def task3():
    numbers = [random.randint(-25, 25) for _ in range(50)]
    A1 = [x for x in numbers if x > 0]
    A2 = [x for x in numbers if x < 0]
    return A1, A2

# Приклад використання
result = task3()
print(result)
# Вивід: ([15, 8, 4, ...], [-23, -19, -6, ...])
```
### Завдання 4
Функція task4 приймає значення my_string, підраховує кількість символів “а” у тексті. Повертає кількість символів “а”.
```python
def task4(my_string):
    count_a = my_string.count('а')
    return count_a

# Приклад використання
my_string = "banana"
result = task4(my_string)
print(result)
# Вивід: 3
```
### Завдання 5
Функція task5 приймає значення my_string. Замінює “GOOD” на “NICE”, виконує розподіл рядка по пробілу та обчислює кількість слів. Повертає значення modified_str, word_count.
```python
def task5(my_string):
    modified_str = my_string.replace("GOOD", "NICE")
    word_count = len(modified_str.split())
    return modified_str, word_count

# Приклад використання
my_string = "GOOD morning everyone"
result = task5(my_string)
print(result)
# Вивід: ('NICE morning everyone', 3)
```
### Завдання 6
Функція task6 підсумовує всі елементи списку від 1 до 5 і повертає значення total_sum.
```python
def task6():
    total_sum = sum([1, 2, 3, 4, 5])
    return total_sum

# Приклад використання
result = task6()
print(result)
# Вивід: 15
```
### Завдання 7
Функція task7 приймає значення my_list, знаходить числа, що діляться на 7 і кратні 5, записує їх у масив result. Повертає значення result.
```python
def task7(my_list):
    result = [x for x in my_list if x % 7 == 0 and x % 5 == 0]
    return result

# Приклад використання
my_list = [35, 70, 14, 21, 50]
result = task7(my_list)
print(result)
# Вивід: [35, 70]
```
# Висновки
Мета роботи досягнута. Було розглянуто основні операції з рядками та списками, використано цикли та оператори для вирішення задач. Реалізовано функції, які демонструють правильну роботу з різними структурами даних у Python.
