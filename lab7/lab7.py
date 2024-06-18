def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Error: Please enter a valid numeric value for age."

def task2(num1, num2):
    try:
        return num1 * num2
    except TypeError:
        return "Error: Please enter valid numeric values for numbers."

def task3(input_str):
    try:
        return len(input_str)
    except TypeError:
        return "Error: Please enter a string, not a numeric value."


def task4(numbers_list):
    try:
        return sum(numbers_list)
    except TypeError:
        return None

def task5(data):
    try:
        results = []
        for name, grades in data:
            avg_grade = sum(grades) / len(grades)
            results.append((avg_grade, name))
        return results
    except Exception as e:
        return "List processing error!"

