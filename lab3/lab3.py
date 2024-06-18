
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

def task2(A, B, C):
    total_cost = sum([B[i] * C[i] for i in range(len(A))])
    average_price = sum(C) / len(C)
    most_stocked_item = A[B.index(max(B))]
    return total_cost, average_price, most_stocked_item

def task3():
    numbers = [random.randint(-25, 25) for _ in range(50)]
    A1 = [x for x in numbers if x > 0]
    A2 = [x for x in numbers if x < 0]
    return A1, A2

def task4(my_string):
    count_a = my_string.count('а')
    return count_a

def task5(my_string):
    modified_str = my_string.replace("GOOD", "NICE")
    word_count = len(modified_str.split())
    return modified_str, word_count

def task6():
    total_sum = sum([1, 2, 3, 4, 5])
    return total_sum

def task7(my_list):
    result = [x for x in my_list if x % 7 == 0 and x % 5 == 0]
    return result

