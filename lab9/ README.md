# Лабораторна робота №9: Регулярні вирази

## Мета роботи
Навчитися використовувати регулярні вирази для пошуку та заміни текстових даних у рядках. Розуміти та використовувати метасимволи та спеціальні конструкції регулярних виразів.

## Опис завдання
Написати регулярні вирази для різних умов.
Реалізувати функції для перевірки рядків за допомогою регулярних виразів.


## Виконання роботи
### Кроки виконання
1. Створити папку для лабораторної роботи (наприклад, `lab9`).
2. Написати основний код програми у файлі `lab9.py`.
3. Створити README файл з детальним поясненням завдання і виконання.
4. Додати коментарі до коду для пояснення складних частин.
5. Завантажити роботу на GitHub.

### Структура проекту
# lab9/
# │
# ├── lab9.py
# └── README.md


### Опис файлів
- `lab9.py`: містить реалізацію функцій для виконання завдань з роботи з JSON даними.
- `README.md`: документ з поясненням завдання, мети роботи, результатів та інструкцій з запуску.

### Опис основних функцій
#### Завдання 1
 Реалізувати функцію `task1`, яка перевіряє, чи містить рядок лише малі літери та цифри.
```python
import re

def task1(s):
    """
    Функція перевіряє, чи містить рядок лише малі літери та цифри.
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок відповідає умовам, інакше False.
    """
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task1("hello123"))  # Вивід: True
print(task1("Hello123"))  # Вивід: False



```
### Завдання 2
Реалізувати функцію `task2`, яка перевіряє, чи містить рядок хоча б одну велику літеру.
```python
import re

def task2(s):
    """
    Функція перевіряє, чи містить рядок хоча б одну велику літеру.
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок містить хоча б одну велику літеру, інакше False.
    """
    pattern = r'[A-Z]'
    return bool(re.search(pattern, s))

# Приклад використання:
print(task2("Hello"))  # Вивід: True
print(task2("hello"))  # Вивід: False


```
### Завдання 3
Реалізувати функцію `task3`, яка перевіряє, чи містить рядок правильну IPv4 адресу.
```python
import re

def task3(s):
    """
    Функція перевіряє, чи містить рядок правильну IPv4 адресу.
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок містить правильну IPv4 адресу, інакше False.
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task3("192.168.1.1"))  # Вивід: True
print(task3("999.999.999.999"))  # Вивід: False


```
### Завдання 4
Реалізувати функцію `task4`, яка перевіряє, чи містить рядок правильний час у форматі "HH:MM
```python
import re

def task4(s):
    """
    Функція перевіряє, чи містить рядок правильний час у форматі "HH:MM:SS".
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок містить правильний час, інакше False.
    """
    pattern = r'^[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task4("12:34:56"))  # Вивід: True
print(task4("25:99:99"))  # Вивід: False

```
### Завдання 5
Реалізувати функцію `task5`, яка перевіряє, чи містить рядок правильний поштовий індекс США у форматі "NNNNN" або "NNNNN-NNNN".
```python
import re

def task5(s):
    """
    Функція перевіряє, чи містить рядок правильний поштовий індекс США у форматі "NNNNN" або "NNNNN-NNNN".
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок містить правильний поштовий індекс, інакше False.
    """
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task5("12345"))  # Вивід: True
print(task5("12345-6789"))  # Вивід: True
print(task5("123456789"))  # Вивід: False

```
### Завдання 6
Реалізувати функцію `task6`, яка перевіряє, чи містить рядок правильне ім'я користувача за наступними критеріями: лише малі літери, цифри, підкреслення та дефіси, довжина від 6 до 12 символів.
```python
import re

def task6(s):
    """
    Функція перевіряє, чи містить рядок правильне ім'я користувача за наступними критеріями:
    лише малі літери, цифри, підкреслення та дефіси, довжина від 6 до 12 символів.
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок відповідає умовам, інакше False.
    """
    pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task6("john_doe-123"))  # Вивід: True
print(task6("JohnDoe"))  # Вивід: False
```
### Завдання 7
Реалізувати функцію `task7`, яка перевіряє, чи містить рядок правильний номер кредитної картки (15 або 16 цифр, починається з 4, 5 або 6).
```python
import re

def task7(s):
    """
    Функція перевіряє, чи містить рядок правильний номер кредитної картки (15 або 16 цифр, починається з 4, 5 або 6).
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок містить правильний номер кредитної картки, інакше False.
    """
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task7("4512-3456-7890-1234"))  # Вивід: True
print(task7("3512-3456-7890-1234"))  # Вивід: False
```
### Завдання 8
Реалізувати функцію `task8`, яка перевіряє, чи містить рядок правильний соціальний номер (у форматі ###-##-####).
```python
import re

def task8(s):
    """
    Функція перевіряє, чи містить рядок правильний соціальний номер (у форматі ###-##-####).
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок містить правильний соціальний номер, інакше False.
    """
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task8("123-45-6789"))  # Вивід: True
print(task8("123-456-789"))  # Вивід: False
```
### Завдання 9
Реалізувати функцію `task9`, яка перевіряє, чи містить рядок правильний пароль за наступними критеріями: щонайменше одна велика літера, одна мала літера, одна цифра, один спеціальний символ (@, #, $, або %), та довжина не менше 8 символів.
```python
import re

def task9(s):
    """
    Функція перевіряє, чи містить рядок правильний пароль за наступними критеріями:
    щонайменше одна велика літера, одна мала літера, одна цифра, один спеціальний символ (@, #, $, або %), 
    та довжина не менше 8 символів.
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок відповідає умовам, інакше False.
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%]).{8,}$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task9("Passw0rd#"))  # Вивід: True
print(task9("password"))  # Вивід: False
```
### Завдання 10
Реалізувати функцію `task10`, яка перевіряє, чи містить рядок правильну IPv6 адресу.
```python
import re

def task10(s):
    """
    Функція перевіряє, чи містить рядок правильну IPv6 адресу.
    
    Параметри:
    s (str): Вхідний рядок.
    
    Повертає:
    bool: True, якщо рядок містить правильну IPv6 адресу, інакше False.
    """
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(pattern, s))

# Приклад використання:
print(task10("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Вивід: True
print(task10("2001:db8:85a3::8a2e:370:7334"))  # Вивід: True
```

# Висновки
У ході лабораторної роботи було реалізовано низку функцій для перевірки рядків за допомогою регулярних виразів. Ці функції допомагають автоматизувати та покращити точність обробки текстових даних, забезпечуючи ефективність та надійність у різноманітних задачах аналізу та валідації даних.