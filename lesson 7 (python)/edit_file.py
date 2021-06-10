##  !!! УКАЗЫВАЮ ПОЛНЫЙ ПУТЬ К ФАЙЛУ,Т.К. PYTHON CELL НЕ ВИДИТ ЕГО !!!
import sys
import datetime

path_file = 'C:/Users/3com/Desktop/Project/data_engineer_training/lesson 7 (python)/test.csv'
path_log = 'C:/Users/3com/Desktop/Project/data_engineer_training/lesson 7 (python)/log.txt'
##ЧТЕНИЕ ФАЙЛА

# способ 1
# создем объект типа файл. Указываем месторасположение и тип (r - чтение,w - перезапись,a - дозапись)
# кодировка, используемая для декодирования или кодирования файла
file = open(path_file, 'r', encoding='utf-8')
# смтотрим что за объект
print('тип объекта: ', type(file), '\n')
# смотрим тип данных и  содержимое
text_list = file.readlines()
print('тип', type(text_list))
print('содержимое', text_list[0:5])

# text_string = file.read()
# print('тип', type(text_string))
# print('содержимое', text_string, '\n')
# закрываем стрим
file.close

## способ 2
# With ... as - менеджеры контекста
with open(path_file, 'r', encoding='utf-8') as file:
    print('тип объекта: ', type(file))
    text_string = file.read()
print(text_string)

with open(path_file, 'r', encoding='utf-8') as file:
    print('тип объекта: ', type(file))
    text_list = file.readlines()
print(text_list)

## ЗАПИСЬ ФАЙЛА
# изменим последнюю строчку
print('смотрим последний элемент массива', text_list[-1])
print('смортим последние два символа последнего элемента массива', text_list[-1][-2:])
# перезаписываем последний элемент массива на срез старой строки до последних двух символов и
# довлением новых символов
text_list[-1] = text_list[-1][:-2] + '44'
print('смотрим последний измененый элемент массива', text_list[-1])

# w - перезапись, a - дозапись
# перезаписываем файл по способу 2
with open(path_file, 'w', encoding='utf-8') as file:
    file.writelines(text_list)

## создание Log файла

# простой лог файл
sys.stdout = open(path_log, 'a')
print('простой лог', datetime.datetime.now())
sys.stdout.close()


## лог файл с отловом ошибок
try:
    sys.stdout = open(path_log, 'a')
    print('лог c try except ', datetime.datetime.now())
    print(10/0)
except Exception as ex:
    sys.stderr = open(path_log, 'a')
    print(ex)
    sys.stderr.close()
finally:
    sys.stdout.close()

