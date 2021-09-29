--  Максим

1.1 Вывести все поля по subscriber_information.*/
select * from data_set.subscriber_information

1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)*/

select * from data_set.subscriber_information si
where si.connection_date >= '2020-01-15'

1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)

в1

select connection_date, count(connection_date) from data_set.subscriber_information
group by connection_date
having connection_date > '2020-01-15'

в2

select connection_date, count(connection_date) from data_set.subscriber_information
where connection_date > '2020-01-15'
group by connection_date



1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices

select connection_date, count(connection_date), max(number_of_tv_devices),max(number_of_internet_devices) from data_set.subscriber_information
group by connection_date
having connection_date > '2020-01-15'



1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.
(???Думал как то с with rollup сделать, не понял как,
типа group by `connection_date`,comment_when_сonnecting
with rollup;)

вариант 1

select connection_date, count(comment_when_сonnecting),
sum(case comment_when_сonnecting when'bad' then 1 else 0 end) as bad,
sum(case comment_when_сonnecting when'good' then 1 else 0 end) as good from data_set.subscriber_information
group by connection_date


вариант 2

select distinct connection_date, si_2.bad, si_3.good from data_set.subscriber_information si_1
left join (select connection_date, count(comment_when_сonnecting) as bad from data_set.subscriber_information
where comment_when_сonnecting ='bad'
group by connection_date) si_2 using (connection_date)
left join (select connection_date, count(comment_when_сonnecting) as good from data_set.subscriber_information
where comment_when_сonnecting ='good'
group by connection_date) si_3 using (connection_date)


2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!

select * from data_set.subscriber_information
left join  period_traffic using(id_abon)

select si.*, pt.day, pt.traffic_gb from data_set.subscriber_information si
left join  period_traffic pt
on pt.id_abon=si.id_abon

2.2 Сделать LJ subscriber_information(основная) и period_traffic.
	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
    В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).

select day,max(traffic_gb)  from data_set.subscriber_information
left join  period_traffic using(id_abon)
where connection_date >= '2020-01-13'
group by day



2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.

select day, traffic_gb from data_set.subscriber_information
left join period_traffic using(id_abon)
where comment_when_сonnecting ='good' and connection_date >= '2020-01-13'


2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении, а так-же были подключены менее
                     2020-02-15, а только чей трафик
	в промежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) был не более 100 GB. !!!


 опять до конца не понял задание, то ли суммарный трафик абонентов, то ли за день и сделал и так и так



--суммарный трафик < 100 (Дениска, а почему having позволяет обратиться к псевдониму sum_traf, если, по идее, он обрабатывается раньше селекта?)

  select count(*) from (select  id_abon, sum(traffic_gb) as sum_traf from  subscriber_information
 left join period_traffic using(id_abon)
 where connection_date < '2020-01-15' and day between '2020-02-01' and '2020-02-15' and comment_when_сonnecting = 'bad'
 group by id_abon
 having sum_traf < 100
 ) as pt

--трафик по дням < 100

select count(*) from (select  distinct id_abon from  subscriber_information
 left join period_traffic using(id_abon)
 where connection_date < '2020-01-15' and day between '2020-02-01' and '2020-02-15' and comment_when_сonnecting = 'bad'
 and traffic_gb < 100) as pt

 -- Софья
 1.1 SELECT *
    FROM subscriber_information

1.2 SELECT *
    FROM subscriber_information
    WHERE connection_date >= '2020.01.15'

1.3 SELECT connection_date, COUNT(connection_date) as "кол-во"
    FROM subscriber_information
    WHERE connection_date > '2020.01.15'
    GROUP BY connection_date
    with rollup

1.4 SELECT connection_date, COUNT(connection_date) as "кол-во", MAX(number_of_tv_devices) as "TV dev",
    MAX(number_of_internet_devices) as "Internet"
    FROM subscriber_information
    WHERE connection_date > '2020.01.15'
    GROUP BY connection_date
    with rollup

1.5 SELECT t3.connection_date as "Дата подключения", t3.Comment_vsego as "Всего коммент. в дату",
    t3.Comment_good as "Кол-во хороших комментариев",
    (t3.Comment_vsego-t3.Comment_good) as "Кол-во плохих комментариев"
    FROM
    (SELECT t1.connection_date as connection_date, t1.Comment_vsego as Comment_vsego,
    (CASE
    WHEN t2.Comment_good is NULL THEN 0
    ELSE t2.Comment_good
    END) as Comment_good
    FROM
    (SELECT connection_date, COUNT(comment_when_сonnecting) as Comment_vsego
    FROM subscriber_information
    GROUP BY connection_date) t1 left join
    (SELECT connection_date, COUNT(*) as Comment_good
    FROM subscriber_information
    where comment_when_сonnecting = 'good'
    GROUP BY connection_date) t2 on t1.connection_date = t2. connection_date) t3


2.1 Select t1.*, t2.day, t2.traffic_gb
    FROM subscriber_information t1 left join period_traffic t2 on t1.id_abon = t2.id_abon

2.2 Select day, MAX(traffic_gb) as Max_traffic
    FROM
    subscriber_information t1 left join period_traffic t2 on t1.id_abon = t2.id_abon
    where connection_date >= '2020-01-13'
    GROUP BY day

2.3 Select day, traffic_gb
    FROM
    subscriber_information t1 left join period_traffic t2 on t1.id_abon = t2.id_abon
    where connection_date >= '2020-01-13' and comment_when_сonnecting = 'good'

2.4 SELECT COUNT(DISTINCT t1.id_abon)
    FROM
    period_traffic t1 left join subscriber_information t2 on t1.id_abon = t2.id_abon
    where comment_when_сonnecting = 'bad'
    and connection_date < '2020-01-15'
    and day >= '2020-02-01' and day <= '2020-02-15'
    and traffic_gb < 100