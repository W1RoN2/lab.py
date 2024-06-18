
# Task 1
def task1(dict_list):
    merged_dict = {}
    for d in dict_list:
        merged_dict.update(d)
    return merged_dict

# Task 2
def task2(string):
    arr = array.array('i', [7, 8, 9, 10])
    bytes_representation = arr.tobytes()
    return f"array1: {arr}\nBytes: {bytes_representation}\narray2: {arr}"

# Task 3
def task3(arr):
    unique_arr = list(OrderedDict.fromkeys(arr))
    return unique_arr

# Task 4
def task4(arr):
    full_range = set(range(10, 21))
    missing_number = full_range - set(arr)
    return missing_number.pop()

# Task 5
def task5(data):
    unique_values = {item['V'] for item in data if 'V' in item}
    return list(unique_values)

# Task 6
def task6(data):
    num_combinations = 1
    for d in data:
        num_combinations *= len(d)
    return num_combinations

# Task 7
def task7(data):
    sorted_keys = sorted(data, key=data.get, reverse=True)
    return sorted_keys[:3]

# Task 8
def task8(dict_list):
    combined_values = {}
    for d in dict_list:
        key = d['item']
        if key in combined_values:
            combined_values[key] += d['amount']
        else:
            combined_values[key] = d['amount']
    return combined_values
