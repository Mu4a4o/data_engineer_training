# pip install pandas
# pip install mysql-connector-python
##
import pandas as pd
import mysql.connector

pd.set_option('display.max_columns', None)

bd = 'data_set'
uspost = 'den'
pspost = 'mu4a4o313'
host = '127.0.0.1'
port = 3308
postgreSQLTable = 'subscriber_information'

SQLConnection = mysql.connector.connect(user = uspost, password = pspost,
                              host = host,
                              port = port,
                              database = bd)

get_sql = f'select * from {postgreSQLTable}'
df = pd.read_sql(get_sql, SQLConnection)
print(df)

SQLConnection .close()

## просмотр dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
print(type(df))
print(df.head(n=5))
## колличество полей
print('колличество строк')
print(df.shape[0])
## типы полей
print('тип полей')
print(df.dtypes)


## нейминг полей
name_columns= ['ид_абонента', 'имя', 'фамилия', 'дата_подключения', 'доверительный_платеж', 'колл_инт_устр', 'колл_тв_устр', 'коммент_при_подкл']
df.columns = name_columns
print('нейминг полей')
print(df.head(n=5))

## статистические методы
'''
.max() Максимум
.min() Минимум
.mean() Среднее значение
.sum() Сумма
.count() Количество непустых элементов
.std() Стандартное отклонение
'''
## Вызов методов
print(df['колл_инт_устр'].max())
print(df['колл_инт_устр'].min())

## Метод describe показывает основные статистические характеристики данных по каждому числовому признаку (типы int и float)
# : число непропущенных значений, среднее, стандартное отклонение, мин значеиине, 0.25 0.50 0.75 квартили, макс значение
print(df.describe())

## Чтобы посмотреть статистику по нечисловым признакам (object или bool)
print(df.describe(include = ['object']))

## меняем на тип дата
print('меняем на тип дата')
df['дата_подключения'] =  pd.to_datetime(df['дата_подключения'], format='%Y-%m-%d')
print(df.dtypes)
## форматы времени %H:%M:%S


## фильтрация
print('фильтрация')
print(df[df['коммент_при_подкл']=='good'].head(n=5))

## множественная фильтрация
print('множественная фильтрация')
print(df[(df['коммент_при_подкл'] =='good')&(df['колл_инт_устр']== 2)])

## фильтр с статистические методом
print(df[(df['коммент_при_подкл'] =='good')&(df['колл_тв_устр']==df['колл_тв_устр'].max())])

## только максимальный номер
print('максимальный номер')
print(df[(df['коммент_при_подкл'] =='good')&(df['дата_подключения']=='2020-01-27')]['колл_тв_устр'].max())
# Проверка
print(df[(df['коммент_при_подкл'] =='good')&(df['дата_подключения']=='2020-01-27')])

## оставляем нужные поля в другом df
print('оставляем нужные поля в другом df')
df_only_col= df[['ид_абонента','дата_подключения']]
print(df_only_col.head(n=5))


# from sqlalchemy import create_engine
# # выгрузка в файл или postgres
# # сохранение в файл
# df_only.to_csv('CSV/tss_only.txt',sep=';',encoding='utf-8',index=None)

# # открываем csv .
# # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# df = pd.read_csv('CSV/tss.csv', # путь
#     sep=',', # разделитель
#     skiprows=100, # пропустить строки в начале
#     nrows= 10000, # загрузить строки
#     header=None, # названия полей отстутсвует
#     usecols=[i for i in range(1,25)]) # выбрать нужные поля по индексу

#



# # группирование таблицы
# # группирование  по кол-ву отнисительно филиала географии контакта
# print('группирование по кол-ву отнисительно филиала географии контакта')
# display(df_new.groupby(['филиал географии контакта']).count())
# # группирование по кол-ву отнисительно филиала географии контакта и сортировка таблицы по номеру
# print('группирование по кол-ву отнисительно филиала географии контакта и сортировка таблицы по номеру')
# display(df_new.groupby(['филиал географии контакта']).count().sort_values(['номер'],ascending=True).sort_values(['номер заявки/CTN контакта'],ascending=True))
#
#
# # уникальные значения
# print('уникальные значения')
# display(df_new.groupby(['филиал географии контакта'])['номер'].nunique().sort_values(ascending=True))
#
# # сводные таблицы
# '''
# values мы передаем ту колонку, по которой нам нужно строить сводные данные, применяя агрегирующую функцию кол-во.
# index передадим ту колонку, данные которой будут представлены строками сводной таблицы.
# columns передаем колонку, значения которой будут в столбцах.
# aggfunc передаем агрегирующую функцию.
# margins итоговые значения.
# '''
# display(df_new.head(5))
# pivot = df_new.loc[df_new['филиал географии контакта'].isin(['OMS','KMR','KRS'])].pivot_table(values=['номер'],
# index=['статус'],
# columns=['филиал географии контакта'],
# aggfunc='count',
# margins=True)
# display(pivot)
#
# #fill_value заменить NaN на 0
# pivot = df_new.loc[df_new['филиал географии контакта'].isin(['OMS','KMR','KRS'])].pivot_table(values=['номер'],
# index=['статус'],
# columns=['филиал географии контакта'],
# aggfunc='count',
# margins=True,
# fill_value=0)
# display(pivot)
