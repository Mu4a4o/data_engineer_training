# pip install names
# pip install sqlalchemy
##
import uuid  # генератор uuid (36 симоволов)
import names  # генератор имен
import random
import pandas as pd
import numpy as np
import sys
import datetime
from sqlalchemy import create_engine
# Сброс ограничений на количество выводимых рядов
#pd.set_option('display.max_rows', None)

#Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
#pd.set_option('display.max_colwidth', None)

bad_good = ['good', 'bad']
path_file = '/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 20 (pandas,generation)/big_si.csv'
path_file_excel = '/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 20 (pandas,generation)/big_si.xlsx'
bd = 'data_set'
us = 'den'
ps = 'mu4a4o313'
host = '127.0.0.1'
port = 3308
SQLTable = 'subscriber_information_big'

# for i in range(2):
#     print(i)
#     id_abon = uuid.uuid1()
#     first_name = names.get_first_name()
#     last_name = names.get_last_name()
#     connection_date = f"2020-{random.randrange(1, 13)}-{random.randrange(1, 30)}"
#     trust_payment = random.randrange(0, 2)
#     number_of_internet_devices = random.randrange(1, 3)
#     number_of_tv_devices = random.randrange(1, 6)
#     comment_when_сonnecting = bad_good[random.randrange(0, 2)]
#     string_add = f"{id_abon};" \
#                  + f"{first_name};" \
#                  + f"{last_name};" \
#                  + f"{connection_date};" \
#                  + f"{trust_payment};" \
#                  + f"{number_of_internet_devices};" \
#                  + f"{number_of_tv_devices};" \
#                  + f"{comment_when_сonnecting}\n"
#     # w - перезапись, a - дозапись
#     # перезаписываем файл по способу 2
#     with open(path_file, 'a', encoding='utf-8') as file:
#         file.writelines(string_add)
## выгужаем из CSV period_traffic
df_si = pd.read_csv(path_file,  # путь
                    sep=';',  # разделитель
                    # skiprows=1, # пропустить строки в начале
                    # nrows= 5, # загрузить строки
                    header=None,  # строка названия полей
                    # usecols=[i for i in range(0,2)] # выбрать нужные поля по индексу
                    )
# ренейминг
name_columns = ['id_abon', 'first_name', 'last_name', 'connection_date', 'trust_payment', 'number_of_internet_devices',
                'number_of_tv_devices', 'comment_when_сonnecting']
df_si.columns = name_columns
print(df_si.head(n=5))

# использование оперативной памяти в байтах
print(sys.getsizeof(df_si))

# подробная информация о df_si. Кол-во инд, типы полей,использование оперативной памяти в округлении
print(df_si.info(memory_usage='deep'))



## Оптимизация df_si


## выбираем оптимальный int для поля 'trust_payment'
# таблица памяти ячеек типа int
int_types = ["int8", "int16", "int32", "int64"]
for it in int_types:
    print(np.iinfo(it))

int_type = 'trust_payment'
col_max = df_si[int_type].astype("int64").max()
col_min = df_si[int_type].astype("int64").min()
if col_max < np.iinfo("int8").max and col_min > np.iinfo("int8").min:
    df_si[int_type] = df_si[int_type].astype("8int")
elif col_max < np.iinfo("int16").max and col_min > np.iinfo("int16").min:
    df_si[int_type] = df_si[int_type].astype("int16")
elif col_max < np.iinfo("int32").max and col_min > np.iinfo("int32").min:
    df_si[int_type] = df_si[int_type].astype("int32")
elif col_max < np.iinfo("int64").max and col_min > np.iinfo("int64").min:
    df_si[int_type] = df_si[int_type].astype("int64")

# выбираем оптимальный int для поля 'number_of_internet_devices'
int_type = 'number_of_internet_devices'
col_max = df_si[int_type].astype("int64").max()
col_min = df_si[int_type].astype("int64").min()
if col_max < np.iinfo("int8").max and col_min > np.iinfo("int8").min:
    df_si[int_type] = df_si[int_type].astype("int8")
elif col_max < np.iinfo("int16").max and col_min > np.iinfo("int16").min:
    df_si[int_type] = df_si[int_type].astype("int16")
elif col_max < np.iinfo("int32").max and col_min > np.iinfo("int32").min:
    df_si[int_type] = df_si[int_type].astype("int32")
elif col_max < np.iinfo("int64").max and col_min > np.iinfo("int64").min:
    df_si[int_type] = df_si[int_type].astype("int64")

# выбираем оптимальный int для поля 'number_of_internet_devices'
int_type = 'number_of_tv_devices'
col_max = df_si[int_type].astype("int64").max()
col_min = df_si[int_type].astype("int64").min()
if col_max < np.iinfo("int8").max and col_min > np.iinfo("int8").min:
    df_si[int_type] = df_si[int_type].astype("int8")
elif col_max < np.iinfo("int16").max and col_min > np.iinfo("int16").min:
    df_si[int_type] = df_si[int_type].astype("int16")
elif col_max < np.iinfo("int32").max and col_min > np.iinfo("int32").min:
    df_si[int_type] = df_si[int_type].astype("int32")
elif col_max < np.iinfo("int64").max and col_min > np.iinfo("int64").min:
    df_si[int_type] = df_si[int_type].astype("int64")

print(df_si.info(memory_usage='deep'))

## узнаем возможные категорариальные поля и даты
# Чтобы посмотреть статистику по нечисловым признакам (object или bool)
print(df_si.describe(include=['object']))

# указываем категориальные типы
cat_type = ['first_name','last_name','comment_when_сonnecting']
df_si[cat_type] = df_si[cat_type].astype('category')

df_si['connection_date'] = pd.to_datetime(df_si['connection_date'], format='%Y-%m-%d')
print(df_si.info(memory_usage='deep'))




## Второй способ
# открываем файл с явными типами
df_si = pd.read_csv(path_file,
                    sep=';',
                    header=None,
                    dtype=
                            {
                                0: 'object',
                                1: 'category',
                                2: 'category',
                                4: 'int8',
                                5: 'int8',
                                6: 'int8',
                                7: 'category',
                            })

print(df_si.info(memory_usage='deep'))

name_columns = ['id_abon', 'first_name', 'last_name', 'connection_date', 'trust_payment', 'number_of_internet_devices',
                'number_of_tv_devices', 'comment_when_сonnecting']
df_si.columns = name_columns

# Форматируем в дату
df_si['connection_date'] = pd.to_datetime(df_si['connection_date'], format='%Y-%m-%d')
print(df_si.info(memory_usage='deep'))

## Добавляем в MySQL партициями

# Подключаем алхимию для добавления данных
# https://docs.sqlalchemy.org/en/13/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector
alchemyEngine = create_engine(f"mysql+mysqlconnector://{us}:{ps}@{host}:{port}/{bd}")
# Делаем коннект
SQLConnection = alchemyEngine.connect()

# кол-во строк которое мы будем считывать за раз
chunksize = 100000
# название полей
name_columns = ['id_abon', 'first_name', 'last_name', 'connection_date', 'trust_payment', 'number_of_internet_devices',
                'number_of_tv_devices', 'comment_when_сonnecting']

# цикл в режиме партиций . Путь к фалу,кодировка файла по дефолту,сепарация,размер одной партиции,режим перебора,все поля в стринг.
for df_si in pd.read_csv(path_file,
                      #encoding="windows-1251",
                      sep=';',
                      chunksize=chunksize,
                      iterator=True,
                      dtype=
                              {
                                  0: 'object',
                                  1: 'category',
                                  2: 'category',
                                  4: 'int8',
                                  5: 'int8',
                                  6: 'int8',
                                  7: 'category',
                              }
                      ):
    # ренейм
    df_si.columns = name_columns
    # Форматируем в дату
    df_si['connection_date'] = pd.to_datetime(df_si['connection_date'], format='%Y-%m-%d')

    # добавляем партицию в Mysql
    df_si.to_sql(SQLTable, SQLConnection, if_exists='append',  index=False)

SQLConnection.close()


## Запись в excel партициями

# кол-во строк которое мы будем считывать за раз
chunksize = 1000000
# название полей
name_columns = ['id_abon', 'first_name', 'last_name', 'connection_date', 'trust_payment', 'number_of_internet_devices',
                 'number_of_tv_devices', 'comment_when_сonnecting']

# номер партиции
i = 0
# цикл в режиме партиций . Путь к фалу,кодировка файла по дефолту,сепарация,размер одной партиции,режим перебора,все поля в стринг.
with pd.ExcelWriter(path_file_excel, mode='a') as writer:
    for df_si in pd.read_csv(path_file,
                           #encoding="windows-1251",
                           sep=';',
                           chunksize=chunksize,
                           iterator=True,
                           dtype=
                                   {
                                       0: 'object',
                                       1: 'category',
                                       2: 'category',
                                       4: 'int8',
                                       5: 'int8',
                                       6: 'int8',
                                       7: 'category',
                                   }
                           ):
         # ренейм
         df_si.columns = name_columns
         # Форматируем в дату
         df_si['connection_date'] = pd.to_datetime(df_si['connection_date'], format='%Y-%m-%d')
         print('start',i)
         df_si.to_excel(writer, sheet_name=f"si_part_{i}")
         print('end', i)
         i += 1
         # на 3 партици вырубаем
         #if i == 3:
         #    break

                                                                                                                                                                                                                                                                                             
