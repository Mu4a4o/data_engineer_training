## JSON ФОРМАТ
import json

## Серелизация JSON-dict в файл
json_path_dict = 'dict.json'
obj_python_dict = {1: '1', 2: '2'}
# метод dump() позволяет заиписывать в файл
with open(json_path_dict , "w") as write_file:
    json.dump(obj_python_dict, write_file)

# Десериализация JSON из файла в объект dict
with open(json_path_dict, 'r') as file:
    data = file.read()
    print('тип data', type(data))
    print('содержание:', data)

obj_json = json.loads(data)
print('тип:', type(obj_json))
print('содержание:', obj_json, '\n')


## Серелизация JSON-list в файл
json_path_list = 'list.json'
obj_python_list = [{1: '1', 2: '2'},{3: '3', 4: '4'}]
with open(json_path_list , "w") as write_file:
    json.dump(obj_python_list, write_file)

# Десериализация JSON из файла в объект list
with open(json_path_list, 'r') as file:
    data = file.read()
obj_json = json.loads(data)
print('тип:', type(obj_json))
print('содержание:', obj_json, '\n')

## Получение через request

import json
import requests
# !!! pip install request
# получаем данный через метод get класса request
response = requests.get("https://jsonplaceholder.typicode.com/todos")
# смотрим модержимое
print('тип:', type(response.text))
print('содержание:', response.text)
todos = json.loads(response.text)
print('тип:', type(todos))
print('содержание:', todos)

## Хранение паролей
json_path_login = '/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 8 (python)/login.json'
with open(json_path_login, 'r') as file:
    data = file.read()










