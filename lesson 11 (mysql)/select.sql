-- ВЫБОР (SELECT)

--ЛИСТ 1, выбор всех записей(*)
select * from 'data_set'.'subscriber_information';

--ЛИСТ 2, выбор определенных колонок,перечисление колонок через запятую
select 'id_abon','first_name','last_name' from 'data_set'.'subscriber_information';

--ВЫБОР С УСЛОВИЕМ (WHERE)

--ЛИСТ 3,больше(>) 0  и(and) меньше(<) 3
select * from 'subscriber_information' where 'number_of_tv_devices' > 0 and 'number_of_tv_devices' < 3

--ЛИСТ 4,не равно(<> и !=) 3
select * from 'subscriber_information' where 'number_of_tv_devices' <> 3;

--ЛИСТ 5, равно(=) 3 ИЛИ(or) равно(=) 2
select * from 'subscriber_information' where 'umber_of_tv_devices'= 3  or 'umber_of_tv_devices' = 2;

--ЛИСТ 6, только не пустое(id not null)
select * from 'subscriber_information' where  'comment_when_сonnecting ' is not null;

--ЛИСТ 7, только пустые(is null)
select * from 'subscriber_information' where 'comment_when_сonnecting' is null;

--ЛИСТ 8, поиск подстроки(LIKE) везде где есть 'b' в начале,середине или в конце (%b%)
-- LIKE медленный т.к. работает вне индекса
select * from 'subscriber_information' where 'first_name' LIKE ('%b%');

--ЛИСТ 9, поиск между 0 (включая) и 2(включая) через BETWEEN
select * from 'subscriber_information' where 'number_of_tv_devices' BETWEEN  0 and 2
