def task1(s):
    return len(s)

def task2(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '//':
        return num1 // num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Invalid operator"

    def task3(numbers):
    if not numbers:  # Перевірка на порожній список
        return None
    return max(numbers)

