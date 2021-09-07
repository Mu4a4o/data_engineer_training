# pip install pandas
# pip install mysql-connector-python
# pip install openpyxl
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


SQLConnection.close()

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

## сохранение в файл CSV
df.to_csv('/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 18 (pandas)/subscriber_information.txt',sep=';',encoding='utf-8',index=None)

## сохранение в файл EXCEL
df.to_excel('/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 18 (pandas)/subscriber_information.xlsx')

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
print(df['доверительный_платеж'].nunique())

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

## группирование таблицы
print('группирование по кол-ву относительно "дата_подключения" ')
print(df.groupby(['дата_подключения']).count())

## группирование по кол-ву отнисительно "дата_подключения" и сортировка таблицы по "доверительный_платеж"
print('группирование по кол-ву отнисительно "дата_подключения" и сортировка таблицы по "доверительный_платеж"')
print(df.groupby(['дата_подключения']).count().sort_values(['доверительный_платеж'],ascending=True))

## группирование по кол-ву отнисительно "дата_подключения" и сортировка таблицы по "доверительный_платеж".
# Оставляем только два поля!!!
print('группирование по кол-ву отнисительно "дата_подключения" и сортировка таблицы по "доверительный_платеж"')
print(df.groupby(['дата_подключения'])['доверительный_платеж'].nunique().sort_values(ascending=True))

## сводные таблицы
'''
isin фильтрация DF
values мы передаем ту колонку, по которой нам нужно строить сводные данные, применяя агрегирующую функцию кол-во.
index передадим ту колонку, данные которой будут представлены строками сводной таблицы.
columns передаем колонку, значения которой будут в столбцах.
aggfunc передаем агрегирующую функцию.
margins итоговые значения.
fill_value = меняем NaN на 0
'''
print(df.head(5))
pivot = df.loc[df['дата_подключения'].isin(['2020-01-09','2020-01-11','2020-01-01'])].pivot_table(values=['дата_подключения'],
index=['коммент_при_подкл'],
columns=['колл_тв_устр'],
aggfunc='count',
margins=True)
print(pivot)

## !!! NaN не будут учитываться в подсчете (см. Index) Нужно менять NaN на значения
# inplace применяем изменения к существующему df
df["коммент_при_подкл"].fillna("no_comment", inplace = True)
pivot = df.loc[df['дата_подключения'].isin(['2020-01-09','2020-01-11','2020-01-01'])].pivot_table(values=['дата_подключения'],
index=['коммент_при_подкл'],
columns=['колл_тв_устр'],
aggfunc='count',
margins=True,
fill_value=0)
print(pivot)