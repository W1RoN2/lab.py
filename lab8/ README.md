# Лабораторна робота №8: обробки JSON даних

## Мета роботи
Навчитися працювати з JSON даними в Python: парсинг, серіалізація, валідація схем, робота з вкладеними структурами та оновлення даних.

## Опис завдання
Реалізувати функції для роботи з JSON даними:

1. JSON Parsing and Data Retrieval: Парсити JSON файл і повертати список імен осіб старших за вказаний вік.
2. Data Transformation and JSON Serialization: Трансформувати список словників у JSON рядок і записати його у файл.
3. JSON Schema Validation: Валідувати JSON файли на відповідність заданій схемі.
4. Nested JSON Data Handling: Видобувати значення за певним ключем з вкладених структур JSON файлу.
5. Updating JSON Data: Оновлювати дані у JSON файлі на основі вказаної категорії і функції оновлення.

## Виконання роботи
### Кроки виконання
1. Створити папку для лабораторної роботи (наприклад, `lab8`).
2. Написати основний код програми у файлі `lab8.py`.
3. Створити README файл з детальним поясненням завдання і виконання.
4. Додати коментарі до коду для пояснення складних частин.
5. Завантажити роботу на GitHub.

### Структура проекту
# lab8/
# │
# ├── lab8.py
# └── README.md


### Опис файлів
- `lab8.py`: містить реалізацію функцій для виконання завдань з роботи з JSON даними.
- `README.md`: документ з поясненням завдання, мети роботи, результатів та інструкцій з запуску.

### Опис основних функцій
#### Завдання 1
 JSON Parsing and Data Retrieval
 Напишіть функцію task1, яка приймає шлях до файлу JSON і пороговий вік, і повертає список імен осіб, вік яких перевищує заданий поріг.
```python
import json

def task1(file_path, age_threshold):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            names = [person['name'] for person in data if person.get('age', 0) > age_threshold]
            return names
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except json.JSONDecodeError:
        return f"Error: File '{file_path}' is not a valid JSON file."
    except Exception as e:
        return f"Error: {str(e)}"

# Приклад використання:
# Якщо у файлі 'people.json' є записи типу [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
print(task1('people.json', 26))  # Виведе ['John']


```
### Завдання 2
Data Transformation and JSON Serialization
Напишіть функцію task2, яка приймає список словників (кожен з іменем, віком та містом) і шлях до файлу, куди потрібно зберегти JSON-рядок цих даних.
```python
import json

def task2(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error: {str(e)}")

# Приклад використання:
people_data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "Los Angeles"}
]
task2(people_data, 'people.json')  # Створить файл 'people.json' з вмістом відповідно до people_data

```
### Завдання 3
JSON Schema Validation
Напишіть функцію task3, яка приймає JSON-схему та список шляхів до файлів JSON для перевірки. Функція повинна повернути список файлів, які не відповідають заданій схемі.
```python
import json
from jsonschema import validate, ValidationError

def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                validate(data, schema)
        except FileNotFoundError:
            invalid_files.append(f"Error: File '{file_path}' not found.")
        except json.JSONDecodeError:
            invalid_files.append(f"Error: File '{file_path}' is not a valid JSON file.")
        except ValidationError as e:
            invalid_files.append(f"Error in file '{file_path}': {e.message}")
        except Exception as e:
            invalid_files.append(f"Error: {str(e)}")
    return invalid_files

# Приклад використання:
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age"]
}
files_to_validate = ['file1.json', 'file2.json']
print(task3(schema, files_to_validate))



```
### Завдання 4
Nested JSON Data Handling
Напишіть функцію task4, яка приймає шлях до файлу JSON з вкладеними структурами та ключ, який потрібно знайти в цій структурі. Функція повинна повернути список значень, які відповідають заданому ключу на будь-якому рівні вкладеності.
```python
import json

def find_key_in_json(data, key):
    results = []

    def extract_from_dict(obj, key):
        if key in obj:
            results.append(obj[key])
        for k, v in obj.items():
            if isinstance(v, dict):
                extract_from_dict(v, key)
            elif isinstance(v, list):
                extract_from_list(v, key)

    def extract_from_list(obj, key):
        for item in obj:
            if isinstance(item, dict):
                extract_from_dict(item, key)
            elif isinstance(item, list):
                extract_from_list(item, key)

    if isinstance(data, dict):
        extract_from_dict(data, key)
    elif isinstance(data, list):
        extract_from_list(data, key)

    return results

def task4(file_path, key):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return find_key_in_json(data, key)
    except FileNotFoundError:
        return [f"Error: File '{file_path}' not found."]
    except json.JSONDecodeError:
        return [f"Error: File '{file_path}' is not a valid JSON file."]
    except Exception as e:
        return [f"Error: {str(e)}"]

# Приклад використання:
# Якщо у файлі 'data.json' є записи типу [{"person": {"name": "John"}}, {"person": {"name": "Alice"}}]
print(task4('data.json', 'name'))  # Виведе ['John', 'Alice']

```
### Завдання 5
Напишіть функцію task5, яка приймає шлях до файлу JSON, категорію товарів для оновлення і функцію оновлення. Функція оновлення має модифікувати обраний товар відповідно до заданих критеріїв (наприклад, збільшення ціни).
```python
Updating JSON Data
import json

def task5(file_path, category, update_function):
    try:
        with open(file_path, 'r+') as file:
            data = json.load(file)
            for item in data:
                if item.get('category') == category:
                    update_function(item)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Приклад функції оновлення: збільшення ціни на 10%
def increase_price(item):
    if 'price' in item:
        item['price'] *= 1.1

# Приклад використання:
# Якщо у файлі 'products.json' є записи типу [{"name": "Product1", "category": "electronics", "price": 100}]
task5('products.json', 'electronics', increase_price)  # Оновить ціни на електроніку в 'products.json'

```


# Висновки
У ході виконання лабораторної роботи було реалізовано низку функцій для роботи з JSON даними в мові програмування Python. Кожна функція виконує певну операцію з обробки JSON, що включає парсинг, серіалізацію, валідацію схем, роботу з вкладеними структурами та оновлення даних.
