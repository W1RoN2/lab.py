
def task1(numbers):
    return numbers[0] + numbers[1]

def task2(tup):
    return len(tup)

def task3(numbers_tuple):
    sorted_tuple = tuple(sorted(numbers_tuple, reverse=True))
    return sorted_tuple[0]

def task4(tuple_with_dict):
    return tuple_with_dict[0]['name']

def task5(list_of_tuples):
    sorted_tuples = sorted(list_of_tuples, key=lambda x: len(x[0]))
    return sorted_tuples[-1][-1]


def task6(tup_of_lists):
    filtered_numbers = [num for sublist in tup_of_lists for num in sublist if num % 2 == 0]
    product = 1
    for num in filtered_numbers:
        product *= num
    return product

def task7(tuple_of_tuples):
    return sum(t[1] for t in tuple_of_tuples)


