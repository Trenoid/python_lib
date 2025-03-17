import yaml


data = {'name': 'Carol', 'age': 27, 'is_student': False}


yaml_string = yaml.dump(data)
print(yaml_string)


with open('data.yaml', 'w') as file:
    yaml.dump(data, file)


loaded_data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(loaded_data)


with open('data.yaml', 'r') as file:
    loaded_data = yaml.load(file, Loader=yaml.FullLoader)
print(loaded_data)