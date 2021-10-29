#### 1. Создать переменные типа строка,листа,множенства,словаря,кортежа и обогатить их произвольными данными.
type_str = '6, 8.0, 9'
print(type_str, type(type_str), '\n')

type_list = []
type_list.extend(['87',56, 6.0, 6.0])
print(type_list, type(type_list), '\n')

type_set = {23}
type_set.update(['87',56, 6.0, 6.0])
type_set.add(5.0)
print(type_set, type(type_set), '\n')
type_set.discard(5.0)
print(type_set, type(type_set), '\n')

type_dict = {'three': 2, 3: 'five', 4: 0}
print(type_dict, type(type_dict), '\n')
type_dict['four'] = [3]
print(type_dict, type(type_dict), '\n')
type_dict.pop(4)
print(type_dict, type(type_dict), '\n')

type_tuple = (4, '6', 5.0)
print(type_tuple, type(type_tuple), '\n')

####2.Доказать при помощи кода, какие переменные из первой задачи являются immutable,а какие mutable при помощи функции id
a = '3'
print(id(a))
b = [6.0]
print(id(b))
c = {23}
print(id(c))
d = {3: '45'}
print(id(d))
e = (4)
print(id(e), '\n')

a = '3' + '5'
print(id(a))
b.append(6)
print(id(b))
c.add(5.0)
print(id(c))
d = {3:'45'}
d[5] = ['32']
print(id(d))
e = (4) + (9)
print(id(e))

## 
d = (3,[],True)
print(id(d),id(d[1]),d[1])
d[1].append(4)
print(id(d),id(d[1]),d[1])


###Реализовать алгоритм пузырьковой сортировки. Я это не объяснял, но задача преследует следующие цели :
# 1. Гугление. Самостоятельный поиск объяснения логики алгоритма, т.е  не готовую реализацию в виде кода !!!
# 3. Переформатирования мозга. При встрече, мне нужно объяснить код алгоритма, то как ты его понимаешь.
# 3. Циклы и условные конструкции. Решаем вопрос с пониманием циклов и условиях.

### Алгоритм пузырьковой сортировки упаковать в функцию bubble_def, которая обернута в декоратор decor_def,
    #который считает время выполнения bubble_def и выводит информацию в файл start_end.txt.
    #bubble_def принимает на вход произвольный список чисел (int) и возращает отсортированый список.
import time

def decor_def(user_func):
    def wrapper_func():
        first_time = time.time()
        print('запоминам текущее время в first_time', first_time)
        a = user_func()  # Сама функция
        print('получаем разницу', time.time() - first_time)
        return a

    return wrapper_func

@decor_def
def bubble_def():

    mas = [5,7,4,3,8,2]
    for run in range(len(mas)-1):
        for i in range(len(mas)-1):
            if mas[i]>mas[i+1]:
                mas[i],mas[i+1] = mas[i+1],mas[i]
    return mas
bubble_def()



#Создать БД `data_set` и таблицы в ней:
   # `subscriber_information` и `period_traffic` из lesson 12/data_set_2.xlsx (лист 1)

##Создать свои две таблицы. Первая должна быть связующей между `subscriber_information` и второй твоей таблицей.Вторая это основная информация
   #Схема связей:
   #`subscriber_information` <-> первая таблица (FK `subscriber_information`.'id_abon') <-> вторая таблица (FK 'первая таблица'.'id_первой таблицы')
   #Наполнение твоих таблиц не должно противоречить данным, которые есть в таблицах ребят(адреса,штаты,города,тарифы,трафик уже заняты)
   #Тут играет твоя фантазия.

create table `data_set`.`mobil_gsm`
(`id_abon`VARCHAR(100),
`year`INT,
PRIMARY KEY (`year`),
FOREIGN KEY (`id_abon`) REFERENCES `subscriber_information` (`id_abon`));

create table `data_set`.`mobil`
(
`age`INT(5),
`gender`VARCHAR(10),
`year`INT,
`life_time` INT,
FOREIGN KEY (`year`) REFERENCES `mobil_gsm` (`year`));

insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('fdf40c5f-50d4-4d9f-a015-b5aece2aa944',2021);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('fdf40c5f-50d4-4d9f-a015-b5aece2aa944',2020);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('d8e7f123-18f6-4c09-a683-d466ee1217e1',2019);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('c069c890-e499-4593-99ec-163aaedbaa90',2018);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('acbfe937-0329-4ff6-9680-cbe1b866c8d1',2017);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('3f8af854-26a1-449d-a4a7-9bcd06a17088',2016);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('cf177d81-063b-4822-84ee-ceb5f726eb1e',2015);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('6f6a0228-ad56-4b16-ba7d-6af91f0685da',2014);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('20d4dd16-9a85-4e9b-895e-61b4e3e1390d',2013);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('c94977f8-fe0f-4d64-a3bf-29936bc015f8',2012);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('93278b7e-c957-4ce4-9326-639e14594655',2011);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('d511f782-3d04-4622-90f4-02eb8a7c6694',2010);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('ccb53bc6-23e4-41be-b548-4694a7d31494',2009);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('083aa6ce-0702-4521-9815-304e61894018',2008);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('7e84e22a-15da-46dd-88f9-b095425d0c5e',2007);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('0318507c-12d9-4d78-9224-77b82afadad9',2006);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('6e15b129-d4e0-41a7-a3c4-32ea6a4a9623',2005);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('a32c6a3f-2a65-4337-9b5c-0795d0f634e6',2004);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('f236b1d9-3cfd-4879-bf3c-dec6910cf8e0',2003);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('c49f41b1-2675-4cf0-837f-460256d2d25a',2002);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('61518eff-0af4-459e-81ab-0ed58916ab75',2001);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('e2783c9c-176e-4ab0-872c-ca266eb22bf8',2000);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('011379f1-910f-43cf-8600-a404594c32e5',1999);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('78de8503-4c05-4756-b574-59f7f6c9d214',1998);
insert into `data_set`.`mobil_gsm` (`id_abon`,`year`) values ('fe863776-81c9-45c2-b537-3b55ff176cdc',1997);

insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (15,'man',2021,12);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (16,'women',2020,11);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (17,'man',2019,15);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (18,'women',2018,10);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (19,'man',2017,8);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (20,'women',2016,12);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (21,'man',2015,11);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (22,'women',2014,15);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (23,'man',2013,10);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (24,'women',2012,8);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (25,'man',2011,12);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (26,'women',2010,11);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (27,'man',2009,15);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (28,'women',2008,10);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (29,'man',2007,8);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (30,'women',2006,12);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (31,'man',2005,11);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (32,'women',2004,15);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (33,'man',2003,10);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (34,'women',2002,8);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (35,'man',2001,12);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (36,'women',2000,11);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (37,'man',1999,15);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (38,'women',1998,10);
insert into `data_set`.`mobil` (`Age`,`gender`,`year`,`life_time`) values (39,'man',1997,8);

# 1.1 Вывести все поля по subscriber_information.
SELECT * FROM subscriber_information
#1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)
SELECT * FROM subscriber_information WHERE connection_date >= '2020.01.15'
#1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)
SELECT
`connection_date` > '2020.01.15',
COUNT(`connection_date`) OVER (PARTITION BY `connection_date`) as `count_date`
FROM
`subscriber_information`
#1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices
select connection_date, count(connection_date), max(number_of_tv_devices),max(number_of_internet_devices) from data_set.subscriber_information
group by connection_date
having connection_date > '2020-01-15'
#1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.
select connection_date,
sum(if (comment_when_сonnecting = 'good',1,0)) as j,
sum(if (comment_when_сonnecting = 'bad',1,0)) as k
from subscriber_information
group by connection_date
#2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!
select `si`.*, `pt`.`day`,`traffic_gb`
from `subscriber_information` as `si`
left join `period_traffic` as `pt`
on `pt`.`id_abon`=`si`.`id_abon`
#2.2 Сделать LJ subscriber_information(основная) и period_traffic.
	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
    В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).
select day,max(traffic_gb)  from data_set.subscriber_information
left join  period_traffic using(id_abon)
where connection_date >= '2020-01-13'
group by day

#2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.
select `si`.`connection_date`,`comment_when_сonnecting`, `pt`.`day`,`traffic_gb`
from `subscriber_information` as `si`
left join `period_traffic` as `pt` on `si`.`id_abon`=`pt`.`id_abon`
and `connection_date` >= '2020-01-13' and `comment_when_сonnecting` = 'good'
order by `pt`.`traffic_gb` desc
#2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении,
    а так-же были подключены ранее 2020-01-15, и чей трафик был
	в промежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) и не более 100 GB. !!!
select count(*) from (select distinct id_abon from  subscriber_information
 left join period_traffic using(id_abon)
 where connection_date < '2020-01-15' and day between '2020-02-01' and '2020-02-15' and comment_when_сonnecting = 'bad'
 and traffic_gb < 100) as pt

ДЗ для Паши
1.1 Вывести все поля по subscriber_information.

1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)

1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)

1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices

1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.

2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!

2.2 Сделать LJ subscriber_information(основная) и period_traffic.
	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
    В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).

2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.

2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении, а так-же были подключены менее
                     2020-02-15, а только чей трафик
	в пр```````омежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) был не более 100 GB. !!!








































































