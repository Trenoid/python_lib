import pickle


data = {'name': 'Alice', 'age': 30, 'is_student': False}


with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)


with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)