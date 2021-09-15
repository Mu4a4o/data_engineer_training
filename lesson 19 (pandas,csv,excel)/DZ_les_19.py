#
# -- subscriber_information (id_abon PK)
# -- subscriber_information.connection_date - когда был подключен абоненент
# -- subscriber_information.comment_when_сonnecting - довольный/недовольный/нейтральный комментарий абонента при подключении
# -- subscriber_information.number_of_tv_devices - кол-во установленных ТВ устройств при подключении
# -- subscriber_information.number_of_internet_devices - кол-во установленных  ИНТЕРНЕТ устройств при подключении
#
# -- period_traffic (id_abon PK FK --> subscriber_information.id_abon),day PK)
# -- period_traffic.day - дата трафика
# -- period_traffic.traffic_gb - трафик абонентов
#
#
# 1.1 Вывести все поля по subscriber_information.
# 1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)
# 1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)
# 1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices
# 1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.
#
# 2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!
# 2.2 Сделать LJ subscriber_information(основная) и period_traffic.
# 	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
#     В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).
# 2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.
# 2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении,
#     а так-же были подключены ранее 2020-01-15, и чей трафик был
# 	в промежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) и не более 100 GB. !!!

## Софья ##

##Part 1:
import pandas as pd
import mysql.connector
import numpy as np

bd = 'data_set'
uspost = 'den'
pspost = 'mu4a4o313'
host = '127.0.0.1'
port = 3308
postgreSQLTable = 'subscriber_information'

SQLConnection = mysql.connector.connect(user=uspost, password=pspost,
                                        host=host,
                                        port=port,
                                        database=bd)

get_sql = f'select * from {postgreSQLTable}'
SI = pd.read_sql(get_sql, SQLConnection)
SQLConnection.close()

##1.1
# 1.1 Вывести все поля по subscriber_information.
print(SI)
print(SI.columns)

##1.2
# 1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
print(SI[(SI['connection_date'] >= '2020-01-15')])

##1.3
# 1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
SI_only_col = SI[['id_abon', 'connection_date']]
print(SI_only_col[SI_only_col['connection_date'] > '2020-01-15'].groupby(['connection_date']).count())

##1.4
# 1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices
# !!connection_date от '2020.01.15'(не вклюительно)
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
SI_only_col = SI[['id_abon', 'connection_date']]
one = SI_only_col[SI_only_col['connection_date'] > '2020-01-15'].groupby(['connection_date']).count()
SI_only_col_1 = SI[['number_of_tv_devices', 'number_of_internet_devices', 'connection_date']]
other = SI_only_col_1[SI_only_col_1['connection_date'] > '2020-01-15'].groupby(['connection_date']).max()
union = one.merge(other, on='connection_date')
print(union)

##1.5 Способ 1 не ловит 0 где нет ни плохих ни хороших:
# 1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
SI_only_col = SI[['connection_date', 'comment_when_сonnecting']]
one = SI_only_col[SI_only_col['comment_when_сonnecting'] == 'good'].groupby(['connection_date']).count()
one.columns = ['good_comment']
other = SI_only_col[SI_only_col['comment_when_сonnecting'] == 'bad'].groupby(['connection_date']).count()
other.columns = ['bad_comment']
union = one.merge(other, how='outer', on='connection_date')
union['good_comment'] = union['good_comment'].replace(np.nan, 0)
union['bad_comment'] = union['bad_comment'].replace(np.nan, 0)
print(union)

##Способ 2 ловит 0:
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
SI['comment_when_сonnecting'] = SI['comment_when_сonnecting'].replace(np.nan, 0)
SI_only_col = SI[['connection_date', 'comment_when_сonnecting']]
one = SI_only_col[SI_only_col['comment_when_сonnecting'] == 'good'].groupby(['connection_date']).count()
one.columns = ['good_comment']
other = SI_only_col[SI_only_col['comment_when_сonnecting'] == 'bad'].groupby(['connection_date']).count()
other.columns = ['bad_comment']
union = one.merge(other, how='outer', on='connection_date')
union['good_comment'] = union['good_comment'].replace(np.nan, 0)
union['bad_comment'] = union['bad_comment'].replace(np.nan, 0)
vse = SI_only_col.groupby(['connection_date']).count()
vse.columns = ['Всего записей на дату']
union_new = union.merge(vse, how='outer', on='connection_date')
union_new['bad_comment'] = union_new['bad_comment'].replace(np.nan, 0)
union_new['good_comment'] = union_new['good_comment'].replace(np.nan, 0)
print(union_new)

##Part 2:

import pandas as pd
import mysql.connector
import numpy as np

bd = 'data_set'
uspost = 'den'
pspost = 'mu4a4o313'
host = '127.0.0.1'
port = 3308
postgreSQLTable_1 = 'subscriber_information'
postgreSQLTable_2 = 'period_traffic'

SQLConnection = mysql.connector.connect(user=uspost, password=pspost,
                                        host=host,
                                        port=port,
                                        database=bd)

get_sql_1 = f'select * from {postgreSQLTable_1}'
SI = pd.read_sql(get_sql_1, SQLConnection)
get_sql_2 = f'select * from {postgreSQLTable_2}'
PT = pd.read_sql(get_sql_2, SQLConnection)
SQLConnection.close()

##2.1
# 2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!
union = SI.merge(PT, how='left', on='id_abon')
print(union)

##2.2
# 2.2 Сделать LJ subscriber_information(основная) и period_traffic.
# 	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
#     В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
union = SI.merge(PT, how='left', on='id_abon')
union_new = union[['connection_date', 'day', 'traffic_gb']]
one = union_new[union_new['connection_date'] >= '2020-01-13'].groupby(['day']).max()
print(one['traffic_gb'])

##2.3
# 2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
union = SI.merge(PT, how='left', on='id_abon')
union_new = union[['connection_date', 'day', 'traffic_gb', 'comment_when_сonnecting']]
one = union_new[(union_new['connection_date'] >= '2020-01-13') & (union_new['comment_when_сonnecting'] == 'good')]
one_1 = one.drop(columns = ['connection_date', 'comment_when_сonnecting'])
print(one_1)

##2.4
# 2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении,
#     а так-же были подключены ранее 2020-01-15, и чей трафик был
# 	в промежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) и не более 100 GB. !!!
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
PT['day'] = pd.to_datetime(PT['day'], format='%Y-%m-%d ')
union = SI.merge(PT, how='left', on='id_abon')
union_new = union[['id_abon', 'connection_date', 'day', 'traffic_gb', 'comment_when_сonnecting']]
one = union_new[(union_new['connection_date'] < '2020-01-15') & (union_new['comment_when_сonnecting'] == 'bad') & (
            union_new['day'] >= '2020-02-01') & (union_new['day'] <= '2020-02-15') & (union_new['traffic_gb'] < 100)]
print(one['id_abon'].nunique())

## Денис ##
import pandas as pd
import mysql.connector
import numpy as np

#Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

bd = 'data_set'
us = 'den'
ps = 'mu4a4o313'
host = '127.0.0.1'
port = 3308
SQLTable = 'subscriber_information'
SQLTable_2 = 'period_traffic'
SQLConnection = mysql.connector.connect(user=us, password=ps,
                                        port=port,
                                        host=host,
                                        database=bd)

get_sql = f'select * from {SQLTable}'
si = pd.read_sql(get_sql, SQLConnection)
pt = pd.read_sql( f'select * from {SQLTable_2}', SQLConnection)

si['connection_date'] = pd.to_datetime(si['connection_date'], format='%Y-%m-%d ')
pt['day'] = pd.to_datetime(pt['day'], format='%Y-%m-%d ')
SQLConnection.close()

## 1.1 Вывести все поля по subscriber_information.
print(si)

## 1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)
print(si[(si['connection_date'] >= '2020-01-15')].sort_values('connection_date'))

## 1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)
si = si[(si['connection_date'] >= '2020-01-15')].sort_values('connection_date')
print(si.groupby(['connection_date'])['connection_date'].count())

## 1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices
print(si[(si['connection_date'] >= '2020-01-15')].groupby(['connection_date']).agg(tv_max=('number_of_tv_devices', 'max'),
                                           in_max=('number_of_internet_devices', 'max'),
                                           conn_count=('connection_date', 'count')))
## 1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.
si['comment_when_сonnecting_2'] = si['comment_when_сonnecting']
si['comment_when_сonnecting'].replace('bad', np.nan, inplace=True)
si['comment_when_сonnecting_2'].replace('good', np.nan, inplace=True)
print(si[['connection_date','comment_when_сonnecting','comment_when_сonnecting_2']] \
      .groupby(['connection_date']) \
      .agg(good_count=('comment_when_сonnecting', 'count'),
           bad_count=('comment_when_сonnecting_2', 'count')))

## 2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!
print(si.merge(pt, how='left', on='id_abon'))

## 2.2 Сделать LJ subscriber_information(основная) и period_traffic.
# 	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
#     В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).
si_j_pt = si.merge(pt, how='left', on='id_abon')
si_j_pt = si_j_pt[(si_j_pt['connection_date'] >= '2020-01-13')].sort_values('connection_date')
print(si_j_pt.groupby(['day'])['traffic_gb'].max())

## 2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.
si_j_pt = si.merge(pt, how='left', on='id_abon')
si_j_pt = si_j_pt[(si_j_pt['connection_date'] >= '2020-01-13')&(si_j_pt['comment_when_сonnecting'] == 'good')].sort_values('connection_date')
print(si_j_pt[['day','traffic_gb']].sort_values('day'))

## 2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении,
#   а так-же были подключены ранее 2020-01-15, и чей трафик был
# 	в промежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) и не более 100 GB. !!!
si_j_pt = si.merge(pt, how='left', on='id_abon')
print(si_j_pt[((si_j_pt['comment_when_сonnecting'] == 'bad')
                    &(si_j_pt['connection_date'] < '2020-01-15')
                    &(si_j_pt['day'] >= '2020-02-01')
                    &(si_j_pt['day'] <= '2020-02-15')
                    &(si_j_pt['traffic_gb'] < 100))]\
                    ['id_abon'].nunique())
