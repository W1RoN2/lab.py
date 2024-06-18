#Task1
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

    import json

def task2(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error: {str(e)}")

   #Task2
   import json

def task2(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error: {str(e)}")

     #Task3
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

    #Task4
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

    #Task5
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

