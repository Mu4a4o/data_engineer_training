

create database `data_set`;
create table `data_set`.`subscriber_information`
(`id_abon`VARCHAR(50) PRIMARY KEY,
`first_name` VARCHAR(25),
`last_name` VARCHAR(25),
`connection_date` DATE,
`trust_payment` INT,
`number_of_internet_devices` INT,
`number_of_tv_devices` INT,
`comment_when_сonnecting` VARCHAR(100));

-- ВЫБОР (SELECT)

-- ЛИСТ 1, выбор всех записей(*)
select * from `data_set`.`subscriber_information`;

-- ЛИСТ 2, выбор определенных колонок,перечисление колонок через запятую
select `id_abon`,`first_name`,`last_name` from `data_set`.`subscriber_information`;

-- ВЫБОР С УСЛОВИЕМ (WHERE)

-- ЛИСТ 3,больше(>) 0  и(and) меньше(<) 3
select * from `subscriber_information` where `number_of_tv_devices` > 0 and `number_of_tv_devices` < 3;

-- ЛИСТ 4,не равно(<> и !=) 3
select * from `subscriber_information` where `number_of_tv_devices` <> 3;

-- ЛИСТ 5, равно(=) 3 ИЛИ(or) равно(=) 2
select * from `subscriber_information` where `number_of_tv_devices`= 3  or `number_of_tv_devices` = 2;

-- ЛИСТ 6, только не пустое(id not null)
select * from `subscriber_information` where  `comment_when_сonnecting` is not null;

-- ЛИСТ 7, только пустые(is null)
select * from `subscriber_information` where `comment_when_сonnecting` is null;

-- ЛИСТ 8, поиск подстроки(LIKE) везде где есть `b` в начале,середине или в конце (%b%)
-- LIKE медленный т.к. работает вне индекса
select * from `subscriber_information` where `first_name` LIKE ('%b%');

-- ЛИСТ 9, поиск между 0 (включая) и 2(включая) через BETWEEN
select * from `subscriber_information` where `number_of_tv_devices` BETWEEN  0 and 2;

-- ЛИСТ 10, только то что перечислено в списке
select * from `subscriber_information` where `comment_when_сonnecting` in ('bad','good');

-- ЛИСТ 11, исключаем то что перечислено в списке
select * from `subscriber_information` where `comment_when_сonnecting` not in ('bad');

-- ЛИСТ 12,сортировка(ORDER BY) по увеличению(ASC) и уменьшению(DESC)
select * from `subscriber_information` order by `number_of_tv_devices` ASC;

-- ФУНКЦИИ
-- ЛИСТ 13, функция агрегация max() поиск максимального значения
-- 104 строка в EXCEL
select max(`number_of_tv_devices`) from `subscriber_information`;

-- ЛИСТ 14, функция агрегация min() поиск минимального значения
-- 104 строка в EXCEL
select min(`number_of_tv_devices`) from `subscriber_information`;

-- ЛИСТ 15, функция агрегация avg() поиск среднего значения значения
-- 104 строка в EXCEL
select avg(`number_of_tv_devices`) from `subscriber_information`;

-- rand(), возвращает случайное число
select rand();

-- round(), обычное округление
-- ceiling(), округление в ольшую сторону
-- floor(),  округление в меньшую сторону
select rand() as r,
select ceiling() as c,
select floor() as f;

-- now(), текущая дата
select now()

-- timestampdiff(в чем нужна разница,период 1,период 2), разница между датами
select `connection_date`, now() as n,
timestampdiff(year, `connection_date`,now()) as y,
timestampdiff(month, `connection_date`,now()) as m,
timestampdiff(day, `connection_date`,now()) as d,
timestampdiff(hour, `connection_date`,now()) as h from `data_set`.`subscriber_information`;

-- str_to_date(строка,маска), конвертация строки формата маски в формат даты
select str_to_date('01.5,2013 12:59','%d.%m,%Y %H:%i');

-- date_format(дата,маска), конвертация даты в формат строки в формате маски
select date_format(`connection_date`, '%Y%m%d') from `data_set`.`subscriber_information`;

-- concat(1,2,3....), объединение полей
select concat(`first_name`,' ',`last_name`) from `data_set`.`subscriber_information`;




-- оставляем только уникальные строки(distinct *) или ункикальнын записи в поле(distinct `col_name`)
-- select distinct * from `subscriber_information`;
select distinct `number_of_tv_devices` from `subscriber_information`;



