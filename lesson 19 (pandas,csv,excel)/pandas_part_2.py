##
import pandas as pd
import mysql.connector
import numpy as np
# объединение
# https://newtechaudit.ru/pandas-merge-join-concatenate/

bd = 'data_set'
uspost = 'den'
pspost = 'mu4a4o313'
host = '127.0.0.1'
port = 3308
SQL_Table = 'period_traffic_join'
CSV_Table = '/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 18 (pandas)/subscriber_information.txt'
EXL_Table ='/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 19 (pandas,csv,excel)/si.xlsx'
SQLConnection = mysql.connector.connect(user=uspost, password=pspost,
                                        host=host,
                                        port=port,
                                        database=bd)

## выгужаем из MySQL period_traffic
get_sql = f'select * from {SQL_Table}'
df_ptj = pd.read_sql(get_sql, SQLConnection)
print(df_ptj)
df_ptj['day'] = pd.to_datetime(df_ptj['day'], format='%Y-%m-%d ')
print(df_ptj.dtypes)
## выгужаем из CSV period_traffic
df_si = pd.read_csv(CSV_Table,  # путь
                    sep=';',  # разделитель
                    # skiprows=1, # пропустить строки в начале
                    # nrows= 5, # загрузить строки
                    header=0,  # строка названия полей
                    # usecols=[i for i in range(0,2)] # выбрать нужные поля по индексу
                    )
print(df_si)
## ренейминг
name_columns = ['id_abon', 'first_name', 'last_name', 'connection_date', 'trust_payment', 'number_of_internet_devices',
                'number_of_tv_devices', 'comment_when_сonnecting']
df_si.columns = name_columns
print(df_si.head(n=5))


##  создадим на DF  справочник
sprav_week_month = pd.DataFrame({
    'date_month': ["2020-02-01", "2020-02-02", "2020-02-03", "2020-02-04", "2020-02-05", "2020-02-06", "2020-02-07",
                   "2020-02-08", "2020-02-09", "2020-02-10", "2020-02-11", "2020-02-12", "2020-02-13", "2020-02-14",
                   "2020-02-15", "2020-02-16", "2020-02-17", "2020-02-18", "2020-02-19", "2020-02-20", "2020-02-21",
                   "2020-02-22", "2020-02-23", "2020-02-24", "2020-02-25", "2020-02-26", "2020-02-27", "2020-02-28",
                   "2020-02-29"],
    'week': [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
})
print(sprav_week_month)
sprav_week_month['date_month'] = pd.to_datetime(sprav_week_month ['date_month'], format='%Y-%m-%d ')
print(sprav_week_month.dtypes)

# Объединение
## left join
print('left join')
df_ptj = df_ptj.merge(sprav_week_month,
                    how='left', # тип объединения (‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’)
                    left_on='day', # поле левой таблицы
                    right_on='date_month', # поле правой таблицы
                    suffixes=(None, '_right') # добавление префикса к названиям полей в случае их дублирования их названий
                    ,).drop(columns= ['date_month']) # удаляем не нужное дублирующее поле
print(df_ptj)

##inner join
print('inner join')
df_ptj = df_ptj.merge(df_si, how='inner', on='id_abon')
print(df_ptj)

##
print(df_ptj.dtypes)

## метод apply

# инициализируем метод, который принимает значение ячейки(value)
def new_col(value_1,value_2):
    # Если в блоке try нет проблем при выполнении, то возвращает объединеное значение двух полей
    try:
        return str(value_1)+'lesson 24 (python,excel)'+str(value_2)
    # Если в блоке try были проблемы при выполнении, то мы переходим в блок except и делаем нужную нам логику
    except:
        return np.nan
        #return None
        #return 'пусто'
print('применем метод apply')
df_ptj['concat_tv_int'] = df_ptj.apply(lambda row: new_col(row['number_of_internet_devices'],row['number_of_tv_devices']),axis =1)

## проверка
print(df_ptj[['number_of_internet_devices','number_of_tv_devices','concat_tv_int']])

## открываем excel
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
df_si_2 = pd.read_excel(EXL_Table, # путь
    sheet_name=['si_1','si_2']) # выбираем листы
print('si_1')
print(df_si_2['si_1'].shape[0])
print(df_si_2['si_1'].shape[1])
print(df_si_2['si_1'].dtypes)
print(df_si_2['si_1'].head(n=5))
print('\nsi_2')
print(df_si_2['si_2'].shape[0])
print(df_si_2['si_2'].shape[1])
print(df_si_2['si_2'].dtypes)
print(df_si_2['si_2'].head(n=5))

## конкатинация по полям
df_si_concat = pd.concat([df_si_2['si_1'],df_si_2['si_2']])
print(df_si_concat.shape[0])
print(df_si_concat.shape[1])
print(df_si_concat.dtypes)
print(df_si_concat.head(n=5))

