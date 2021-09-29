# Для Оли
"""
Создать функцию к примеру "user_func" (название выбираете свое):
1. "user_func" принимает произвольное количество аргументов.
2. Алгротим должен перемножить все аргументы подданые на вход "user_func" , так-же должна быть проверка на тип INT.
3. "user_func" должна вывести резуальтат перемножения в print, а так-же сделать вернуть (return) его.

"user_func" должна быть обернута в ДЕКОРАТОР "user_decor" (название выбираете свое):
1. "user_decor" введет логирование (stdout,stderr) отработки "user_func" и записывает все в файл "user_log" (название выбираете свое)
Для проверки сделайте сознательную ошибку в "user_func"
2. "user_decor" введет подсчет времени выполнения "user_func" и выводит его в print
"""

#
"""
1. Создать функцию dict_url, которая будет получать на вход URL. 
Она должна вернуть словарь данных, которые мы получили в формате JSON по данному URL
!!! Вы сами должны найти в google URL с "JSON dataset".
!!! Данные могут быть любыми: погода, dataset(Kagle),стоимость валют и т.д.

2. Создать функцию join_dict, которая принимает произвольное количество аргументов в виде словарей.
Она должна вернуть одмн общий словарь, который объединяет все словари подданные на вход этой функции.

3. Создать фукнцию save_file_json, которая принмает на вход словарь и путь с названием json файла.
Она должна преобразить данные словаря и записать в JSON файл

4. Вызвать три функции dict_url и их результаты  оправить в функцию join_dict.
Результат join_dict , отправить в функцию save_file_json.

"""
## Денис
import json
import requests


def dict_url(url):
    response = requests.get(url)
    return json.loads(response.text)


def join_dict(*args):
    for i in range(1, len(args)):
         args[0].update(args[i])
    return args[0]

def save_file_json(dict_value,path_json):
    with open(path_json, "w") as write_file:
        json.dump(dict_value, write_file)


url = {'bitcoin': 'https://api.coincap.io/v2/assets/bitcoin',
       'random_user': 'https://randomuser.me/api/1.3/',
       'nasa_planetary': 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
       }

join_dict_value = join_dict(dict_url(url['bitcoin']),dict_url(url['random_user']),dict_url(url['nasa_planetary']))
save_file_json(join_dict_value, '../lesson 8 (python)/denis_json.json')