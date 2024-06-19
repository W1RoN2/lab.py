# Лабораторна робота №12: Робота з двовимірними матрицями в Python

## Мета роботи
Ознайомитися зі створенням та маніпулюванням двовимірними матрицями в мові програмування Python, навчитися реалізовувати методи для додавання елементів, обчислення суми рядків, транспонування матриць, множення матриць, перевірки симетрії матриць та інших операцій.

## Опис завдання
1. Ознайомлення з класом Matrix, який дозволяє ініціалізувати матрицю з нулів, додавати елементи, обчислювати суму рядків, транспонувати матрицю, множити матриці, перевіряти симетрію та виконувати інші операції.
2. Реалізація функціоналу класу Matrix для зазначених завдань.


## Виконання роботи
### Кроки виконання
1. Створити папку для лабораторної роботи (наприклад, `lab12`).
2. Написати основний код програми у файлі `lab12.py`.
3. Створити README файл з детальним поясненням завдання і виконання.
4. Додати коментарі до коду для пояснення складних частин.
5. Завантажити роботу на GitHub.

### Структура проекту
# lab12/
# │
# ├── lab12.py
# └── README.md


### Опис файлів
- `matrix.py`: містить реалізацію класу `Matrix` для створення та маніпулювання двовимірними матрицями.
- `README.md`: документ з описом завдання, мети роботи, результатів та інструкціями з використання.

### Опис основних функцій
#### Завдання 1: Створення матриці
Конструктор класу `Matrix` ініціалізує двовимірний список з нулів, враховуючи передану кількість рядків та стовпців.
```python
def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.data = [[0] * columns for _ in range(rows)]

```
### Завдання 2:  Додавання елементів до матриці
Метод `add_element` дозволяє додати елемент в конкретну позицію матриці:
```python
def add_element(self, row, column, value):
    if 0 <= row < self.rows and 0 <= column < self.columns:
        self.data[row][column] = value
    else:
        raise IndexError("Index out of range")


```
### Завдання 3: Сума елементів рядків матриці
Метод `sum_of_rows`повертає список сум елементів по кожному рядку матриці:
```python
def sum_of_rows(self):
    return [sum(row) for row in self.data]
```
### Завдання 4: Транспонування матриці
Метод transpose повертає нову матрицю, яка є транспонованою відносно оригінальної:
```python
def transpose(self):
    transposed = Matrix(self.columns, self.rows)
    for i in range(self.rows):
        for j in range(self.columns):
            transposed.data[j][i] = self.data[i][j]
    return transposed
```
### Завдання 5: Множення матриць
Метод `multiply_by` обчислює добуток двох матриць:
```python
def multiply_by(self, other):
    if self.columns != other.rows:
        raise ValueError("Number of columns of the first matrix must be equal to the number of rows of the second matrix")
    
    result = Matrix(self.rows, other.columns)
    for i in range(self.rows):
        for j in range(other.columns):
            for k in range(self.columns):
                result.data[i][j] += self.data[i][k] * other.data[k][j]
    return result
```
### Завдання 6: Перевірка симетричності матриці
Метод `is_symmetric` перевіряє, чи є матриця симетричною:
```python
def is_symmetric(self):
    if self.rows != self.columns:
        return False
    
    for i in range(self.rows):
        for j in range(i + 1, self.columns):
            if self.data[i][j] != self.data[j][i]:
                return False
    return True
```
### Завдання 7: Поворот матриці на 90 градусів
Метод rotate_right повертає нову матрицю, яка є результатом повороту оригінальної матриці на 90 градусів управліч по годинниковій стрілці:
```python
def rotate_right(self):
    rotated = Matrix(self.columns, self.rows)
    for i in range(self.rows):
        for j in range(self.columns):
            rotated.data[j][self.rows - 1 - i] = self.data[i][j]
    return rotated
```
### Завдання 8: Згладжування матриці
Метод flatten повертає одномірний список, що містить усі елементи матриці:
```python
def flatten(self):
    flattened = []
    for row in self.data:
        flattened.extend(row)
    return flattened
```
### Завдання 9: Створення матриці зі списку списків
Статичний метод from_list створює об'єкт матриці з заданого списку списків:
```python
@staticmethod
def from_list(list_of_lists):
    rows = len(list_of_lists)
    columns = len(list_of_lists[0])
    matrix = Matrix(rows, columns)
    for i in range(rows):
        for j in range(columns):
            matrix.data[i][j] = list_of_lists[i][j]
    return matrix
```
### Завдання 10: Вилучення діагоналі матриці
Метод diagonal повертає діагональ матриці як список:
```python
def diagonal(self):
    if self.rows != self.columns:
        raise ValueError("Matrix must be square to extract diagonal")
    
    return [self.data[i][i] for i in range(self.rows)]
```
# Приклади використання класу Matrix
```python
# Створення матриці
matrix = Matrix(2, 3)
print(matrix.data)  # Вивід: [[0, 0, 0], [0, 0, 0]]

# Додавання елементів до матриці
matrix.add_element(1, 2, 10)
print(matrix.data)  # Вивід: [[0, 0, 10], [0, 0, 0]]

# Обчислення суми рядків матриці
matrix = Matrix(2, 3)
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
print(matrix.sum_of_rows())  # Вивід: [15, 0]

# Транспонування матриці
matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data)  # Вивід: [[0, 0], [1, 0], [0, 2]]

# Множення матриць
matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data)  # Вивід: [[14, 0], [0, 0]]

# Перевірка симетричності матриці
matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric())  # Вивід: True

# Поворот матриці на 90 градусів
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data)  # Вивід: [[3, 1], [4, 2]]

# Згладжування матриці
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten())  # Вивід: [1, 2, 3, 4]

# Створення матриці зі списку списків
list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data)  # Вивід: [[1, 2], [3, 4]]

# Вилучення діагоналі матриці
matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal())  # Вивід: [1, 2, 3]
```

# Висновки
Ця лабораторна робота дозволила ознайомитися зі створенням та маніпулюванням двовимірними структурами даних у Python, зокрема матрицями.  Я  розглянув основні операції з матрицями, такі як створення, додавання елементів, обчислення сум рядків, транспонування, множення матриць, перевірку симетричності, поворот на 90 градусів, згладжування та вилучення діагоналі. Кожне завдання було виконано з дотриманням підходів до об'єктно-орієнтованого програмування, що дозволило ефективно використовувати можливості мови Python для роботи з матрицями.
