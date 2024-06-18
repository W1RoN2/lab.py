# Лабораторна робота №10: Об'єктно-орієнтоване програмування в Python

## Мета роботи
Навчитися використовувати основні принципи об'єктно-орієнтованого програмування (ООП) в Python: створення класів, наслідування, поліморфізм та інкапсуляцію.

## Опис завдання
Створити класи для реалізації основних принципів об'єктно-орієнтованого програмування (ООП) у Python.


## Виконання роботи
### Кроки виконання
1. Створити папку для лабораторної роботи (наприклад, `lab10`).
2. Написати основний код програми у файлі `lab10.py`.
3. Створити README файл з детальним поясненням завдання і виконання.
4. Додати коментарі до коду для пояснення складних частин.
5. Завантажити роботу на GitHub.

### Структура проекту
# lab10/
# │
# ├── lab10.py
# └── README.md


### Опис файлів
- `lab10.py`: містить реалізацію функцій для виконання завдань з роботи з JSON даними.
- `README.md`: документ з поясненням завдання, мети роботи, результатів та інструкцій з запуску.

### Опис основних функцій
#### Завдання 1: Створення класу
 Створіть клас Student з наступними атрибутами: name, age, grade.
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Приклад використання:
student = Student(name="Ivan", age=30, grade="2")
print(student.name)  # Вивід: Ivan
print(student.age)   # Вивід: 30
print(student.grade) # Вивід: 2

```
### Завдання 2: Створення методу
Додайте метод display_info() до класу Student, який виводить ім'я, вік та клас студента.
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Приклад використання:
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info())  # Вивід: Name: Ivan, Age: 30, Grade: 2
```
### Завдання 3: Наслідування
Створіть два класи: `Animal` і `Dog`. `Animal`повинен мати атрибути `name` та `sound`. Додайте метод `make_sound()` до `Animal`, який повертає рядок у форматі “[name]: [sound]”. Dog повинен наслідувати `Animal` та мати додатковий атрибут `breed`.
```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"

class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

# Приклад використання:
animal = Animal(name="Lala", sound=" ")
dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz")
print(animal.make_sound())  # Вивід: Lala:  
print(dog.make_sound())     # Вивід: Lala: Auuuuuuu
print(dog.breed)            # Вивід: Spitz

```
### Завдання 4: Поліморфізм
Створіть клас `Bird` з методом `fly()`, який повертає `None`. Потім створіть два підкласи: `Sparrow `та `Penguin`. 
Перевизначте метод `fly()` у `Sparrow`, щоб він повертав рядок “Sparrow flies high”, та у `Penguin`, щоб він повертав рядок “Penguin cannot fly”.
```python
class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

# Приклад використання:
bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly())      # Вивід: None
print(sparrow.fly())   # Вивід: Sparrow flies high
print(penguin.fly())   # Вивід: Penguin cannot fly

```
### Завдання 5: Інкапсуляція
Створіть клас `Encapsulation` з наступними атрибутами: `public`, `_private`, `__protected`.
```python
class Encapsulation:
    def __init__(self, public, _private, __protected):
        self.public = public
        self._private = _private
        self.__protected = __protected

# Приклад використання:
obj = Encapsulation(1, 2, 3)
print(obj.public)  # Вивід: 1
print(obj._private)  # Вивід: 2
print(obj._Encapsulation__protected)  # Вивід: 3
try:
    print(obj.__protected)  # Вивід: AttributeError
except AttributeError as e:
    print(e)  # Вивід: 'Encapsulation' object has no attribute '__protected'


```
### Завдання 6: Прямокутник
Створіть клас `Rectangle`, який має атрибути `width` та `height`, та метод `calculate_perimeter()`, який повертає периметр фігури.
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Приклад використання:
rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter())  # Вивід: 18

```
### Завдання 7: Калькулятор середнього значення
Створіть клас AverageCalculator, який має атрибут numbers та приймає список цілих чисел. Клас повинен мати метод calculate_average(), який повертає середнє арифметичне чисел у списку.
```python
class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

# Приклад використання:
numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average())  # Очікуваний вивід: 12.5

```


# Висновки
У ході лабораторної роботи було розглянуто основні принципи ООП в Python, зокрема створення класів, наслідування, поліморфізм та інкапсуляцію. Виконані завдання дозволили на практиці застосувати ці принципи та створити відповідні класи з різноманітними методами та атрибутами.
