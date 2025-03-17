import json


data = {'name': 'Bob', 'age': 25, 'is_student': True}


json_string = json.dumps(data)
print(json_string)


with open('data.json', 'w') as file:
    json.dump(data, file)


loaded_data = json.loads(json_string)
print(loaded_data)


with open('data.json', 'r') as file:
    loaded_data = json.load(file)
print(loaded_data)