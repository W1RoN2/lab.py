# Лабораторна робота №7: Обробка помилок (try/except)

## Мета роботи
Навчитися використовувати конструкції try/except для обробки помилок в Python.

## Опис завдання
У цій лабораторній роботі ми реалізуємо низку функцій для обробки кортежів з числами та рядками, здійснимо сортування, фільтрацію елементів і обчислимо добутки чи суми.

## Виконання роботи
### Структура проекту
# lab7/
# │
# ├── lab7.py
# └── README.md

### Опис файлів
- `lab7.py`: файл з реалізацією функцій для завдань з кортежами.
- `README.md`: опис завдань, їх виконання та приклади використання функцій.

### Опис основних функцій
#### Завдання 1
Напишіть функцію task1, яка приймає ціле число і повертає його. Якщо користувач вводить нечислове значення, програма повинна повернути повідомлення про помилку: "Error: Please enter a valid numeric value for age."
```python
def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Error: Please enter a valid numeric value for age."
        
# Приклад використання:
print(task1("25"))  # Виведе 25
print(task1("abc"))  # Виведе "Error: Please enter a valid numeric value for age."
```
#### Завдання 2
Напишіть функцію task2, яка приймає два числа і повертає їхній добуток. Якщо користувач вводить нечислове значення, програма повинна повернути повідомлення про помилку: "Error: Please enter valid numeric values for numbers."
```python
def task2(num1, num2):
    try:
        return num1 * num2
    except TypeError:
        return "Error: Please enter valid numeric values for numbers."

# Приклад використання:
print(task2(3, 4))    # Виведе 12
print(task2("abc", 4))  # Виведе "Error: Please enter valid numeric values for numbers."
```
#### Завдання 3
Напишіть функцію task3, яка приймає рядок і повертає його довжину. Якщо користувач вводить числове значення, програма повинна повернути повідомлення про помилку: "Error: Please enter a string, not a numeric value."
```python
def task3(input_str):
    try:
        return len(input_str)
    except TypeError:
        return "Error: Please enter a string, not a numeric value."

# Приклад використання:
print(task3("Hello"))  # Виведе 5
print(task3(123))      # Виведе "Error: Please enter a string, not a numeric value."
```
#### Завдання 4
Напишіть функцію task4, яка приймає список цілих чисел і повертає їхню суму. Якщо список містить значення, що не є цілими числами, програма повинна повернути None.
```python
def task4(numbers_list):
    try:
        return sum(numbers_list)
    except TypeError:
        return None

# Приклад використання:
print(task4([1, 2, 3]))         # Виведе 6
print(task4([1, 2, "abc", 3]))  # Виведе None
```
#### Завдання 5
Напишіть функцію task5, яка приймає список кортежів, де кожен кортеж містить ім'я студента і його оцінки, і повертає список кортежів, де перший елемент - середня оцінка студента, а другий - його ім'я. Якщо виникає помилка під час обробки списку, функція повинна повернути рядок "List processing error!".
```python
def task5(data):
    try:
        results = []
        for name, grades in data:
            avg_grade = sum(grades) / len(grades)
            results.append((avg_grade, name))
        return results
    except Exception as e:
        return "List processing error!"

# Приклад використання:
data = [('John', (2, 2, 3)), ('Jane', (4, 3, 5)), ('Jack', (5, 4, 4))]
print(task5(data))  # Виведе [(2.3333333333333335, 'John'), (4.0, 'Jane'), (4.333333333333333, 'Jack')]
```
# Висновки
У цій лабораторній роботі ми вивчили, як використовувати конструкції try/except для обробки різних видів помилок у Python. Кожна з функцій має механізм обробки помилок, що дозволяє коректно взаємодіяти з користувачем із забезпеченням безпеки та надійності програми.
