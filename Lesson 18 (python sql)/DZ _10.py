##Part 1:
import pandas as pd
import mysql.connector
import numpy as np
bd = 'data_set'
uspost = 'sleephead'
pspost = 'password5'
host = '127.0.0.1'
port = 3306
postgreSQLTable = 'subscriber_information'

SQLConnection = mysql.connector.connect(user = uspost, password = pspost,
                              host = host,
                              port = port,
                              database = bd)

get_sql = f'select * from {postgreSQLTable}'
SI = pd.read_sql(get_sql, SQLConnection)
SQLConnection.close()

##1.1
print(SI)
print(SI.columns)

##1.2
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
print(SI[(SI['connection_date'] >='2020-01-15')])

##1.3
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
SI_only_col = SI[['id_abon', 'connection_date']]
print(SI_only_col[SI_only_col['connection_date'] > '2020-01-15'].groupby(['connection_date']).count())

##1.4
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
SI_only_col = SI[['id_abon', 'connection_date']]
one = SI_only_col[SI_only_col['connection_date'] > '2020-01-15'].groupby(['connection_date']).count()
SI_only_col_1 = SI[['number_of_tv_devices', 'number_of_internet_devices', 'connection_date']]
other = SI_only_col_1[SI_only_col_1['connection_date'] > '2020-01-15'].groupby(['connection_date']).max()
union = one.merge(other, on='connection_date')
print(union)

##1.5 Способ 1 не ловит 0 где нет ни плохих ни хороших:
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
SI['comment_when_сonnecting']=SI['comment_when_сonnecting'].replace(np.nan, 0)
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
uspost = 'sleephead'
pspost = 'password5'
host = '127.0.0.1'
port = 3306
postgreSQLTable_1 = 'subscriber_information'
postgreSQLTable_2 = 'period_traffic'

SQLConnection = mysql.connector.connect(user = uspost, password = pspost,
                              host = host,
                              port = port,
                              database = bd)

get_sql_1 = f'select * from {postgreSQLTable_1}'
SI = pd.read_sql(get_sql_1, SQLConnection)
get_sql_2 = f'select * from {postgreSQLTable_2}'
PT = pd.read_sql(get_sql_2, SQLConnection)
SQLConnection.close()

##2.1
union = SI.merge(PT, how='left', on='id_abon')
print(union)

##2.2
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
union = SI.merge(PT, how='left', on='id_abon')
union_new = union[['connection_date', 'day', 'traffic_gb']]
one = union_new[union_new['connection_date'] >= '2020-01-13'].groupby(['day']).max()
print(one['traffic_gb'])

##2.3
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
union = SI.merge(PT, how='left', on='id_abon')
union_new = union[['connection_date', 'day', 'traffic_gb', 'comment_when_сonnecting']]
one = union_new[(union_new['connection_date'] >= '2020-01-13') & (union_new['comment_when_сonnecting'] == 'good')]
one_1 = one.drop(columns = ['connection_date', 'comment_when_сonnecting'])
print(one_1)

##2.4
SI['connection_date'] = pd.to_datetime(SI['connection_date'], format='%Y-%m-%d ')
PT['day'] = pd.to_datetime(PT['day'], format='%Y-%m-%d ')
union = SI.merge(PT, how='left', on='id_abon')
union_new = union[['id_abon', 'connection_date', 'day', 'traffic_gb', 'comment_when_сonnecting']]
one = union_new[(union_new['connection_date'] < '2020-01-15') & (union_new['comment_when_сonnecting'] == 'bad') & (union_new['day'] >= '2020-02-01') & (union_new['day'] <= '2020-02-15') & (union_new['traffic_gb'] < 100)]
print(one['id_abon'].nunique())