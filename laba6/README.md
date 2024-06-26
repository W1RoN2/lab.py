# Лабораторна робота №6: Кортежі в Python

## Мета роботи
Навчитись працювати з кортежами в Python, їх створення, індексація та використання в різних функціях обробки даних.

## Опис завдання
У цій лабораторній роботі ми реалізуємо низку функцій для обробки кортежів з числами та рядками, здійснимо сортування, фільтрацію елементів і обчислимо добутки чи суми.

## Виконання роботи
### Структура проекту
# lab6/
# │
# ├── lab6.py
# └── README.md

### Опис файлів
- `lab6.py`: файл з реалізацією функцій для завдань з кортежами.
- `README.md`: опис завдань, їх виконання та приклади використання функцій.

### Опис основних функцій
#### Завдання 1
Реалізувати функцію `task1`, яка приймає кортеж із двох чисел і повертає їх суму.

```python
def task1(numbers):
    """
    Функція обчислює суму двох чисел з кортежу.
    
    Параметри:
    numbers (tuple): Кортеж, що містить два числа.
    
    Повертає:
    int: Сума двох чисел.
    """
    return numbers[0] + numbers[1]

# Приклад використання:
numbers = (10, 20)
result = task1(numbers)
print(result)  # Виведе 30
```
### Завдання 2
Реалізувати функцію `task2`, яка приймає кортеж і повертає його довжину.
```python
def task2(tup):
    """
    Функція обчислює довжину кортежу.
    
    Параметри:
    tup (tuple): Вхідний кортеж.
    
    Повертає:
    int: Довжина кортежу.
    """
    return len(tup)

# Приклад використання:
tup = (1, 2, 3, "hello", "world")
result = task2(tup)
print(result)  # Виведе 5
```
### Завдання 3
Реалізувати функцію `task3`, яка сортує кортеж з числами у порядку спадання і повертає перший елемент. 
```python
def task3(numbers_tuple):
    """
    Функція сортує кортеж з числами у порядку спадання і повертає перший елемент.
    
    Параметри:
    numbers_tuple (tuple): Кортеж з числами.
    
    Повертає:
    int: Перший елемент відсортованого кортежу.
    """
    sorted_tuple = tuple(sorted(numbers_tuple, reverse=True))
    return sorted_tuple[0]

# Приклад використання:
numbers_tuple = (5, 1, 9, 3, 7)
result = task3(numbers_tuple)
print(result)  # Виведе 9
```
### Завдання 4
Реалізувати функцію `task4`, яка приймає кортеж, що містить словник, і повертає значення ключа "name" з цього словника.
```python
def task4(tuple_with_dict):
    """
    Функція приймає кортеж, що містить словник, і повертає значення ключа "name" з цього словника.
    
    Параметри:
    tuple_with_dict (tuple): Кортеж із словником, що містить ключ "name".
    
    Повертає:
    str: Значення ключа "name".
    """
    return tuple_with_dict[0]['name']

# Приклад використання:
tuple_with_dict = ({'name': 'John', 'age': 30},)
result = task4(tuple_with_dict)
print(result)  # Виведе 'John'
```
### Завдання 5
Реалізувати функцію `task5`, яка приймає кортеж зі списками кортежів, сортує їх за зростанням за довжиною першого елемента кожного кортежу і повертає останній елемент останнього кортежу.
```python
def task5(list_of_tuples):
    """
    Функція приймає кортеж зі списками кортежів, сортує їх за зростанням за довжиною першого елемента кожного кортежу 
    і повертає останній елемент останнього кортежу.
    
    Параметри:
    list_of_tuples (tuple): Кортеж зі списками кортежів.
    
    Повертає:
    object: Останній елемент останнього кортежу.
    """
    sorted_tuples = sorted(list_of_tuples, key=lambda x: len(x[0]))
    return sorted_tuples[-1][-1]

# Приклад використання:
list_of_tuples = ([(1, 2, 3), (4, 5), (6, 7, 8, 9)], [(10, 11), (12, 13, 14)], [(15, 16), (17, 18, 19, 20)])
result = task5(list_of_tuples)
print(result)  # Виведе (17, 18, 19, 20)
```
### Завдання 6
Реалізувати функцію `task6`, яка фільтрує всі непарні числа у кортежі, їхній добуток та повертає результат.
```python
def task6(tup_of_lists):
    """
    Функція фільтрує всі непарні числа у кортежі, обчислює їхній добуток і повертає результат.
    
    Параметри:
    tup_of_lists (tuple): Кортеж зі списками чисел.
    
    Повертає:
    int: Добуток всіх непарних чисел у кортежі.
    """
    filtered_numbers = [num for sublist in tup_of_lists for num in sublist if num % 2 != 0]
    product = 1
    for num in filtered_numbers:
        product *= num
    return product

# Приклад використання:
tup_of_lists = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
result = task6(tup_of_lists)
print(result)  # Виведе 945 (1 * 3 * 5 * 7 * 9)
```
### Завдання 7
Реалізувати функцію `task7`, яка приймає кортеж зі списками кортежів, де кожний кортеж містить два числа, і повертає суму всіх других елементів кожного кортежу.
```python
def task7(tuple_of_tuples):
    """
    Функція приймає кортеж зі списками кортежів, де кожний кортеж містить два числа, і повертає суму всіх других елементів кожного кортежу.
    
    Параметри:
    tuple_of_tuples (tuple): Кортеж зі списками кортежів, де кожний кортеж містить два числа.
    
    Повертає:
    int: Сума всіх других елементів кожного кортежу.
    """
    return sum(t[1] for t in tuple_of_tuples)

# Приклад використання:
tuple_of_tuples = ([(1, 2), (3, 4), (5, 6)], [(7, 8), (9, 10)])
result = task7(tuple_of_tuples)
print(result)  # Виведе 30 (2 + 4 + 6 + 8 + 10)
```
# Висновки
У цій лабораторній роботі я ознайомився з кортежами в Python та реалізув функції для їх обробки. Кортежі є корисним типом даних для зберігання необмінних послідовностей елементів. Кожна функція виконує своє завдання з використанням кортежів і демонструє їхні можливості в різних сценаріях використання.
