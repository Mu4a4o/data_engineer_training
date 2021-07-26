

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

-- ВЫБОР SELECT
-- ЛИСТ 1, выбор всех записей(*)
select * from `data_set`.`subscriber_information`;

-- ЛИСТ 2, выбор определенных колонок,перечисление колонок через запятую
select `id_abon`,`first_name`,`last_name` from `data_set`.`subscriber_information`;

-- ВЫБОР С УСЛОВИЕМ WHERE

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

-- УСЛОВИЯ IF
-- if(условие, если истина, если не истина), проверка по условию и возврат значений
select `first_name`,
if(`first_name` = 'Rick', 'Рик здесь', 'Рика здесь нет') as `where_is_Rick`
from `data_set`.`subscriber_information`;

-- case, множественное условие when и все остально else
select `connection_date`,
case `connection_date`
    when '2020-01-30' then 'тридцатое'
    when '2020-01-29' then 'двадцать девятое'
    else 'все остальные'
end as `connection_date_varchar`
from `data_set`.`subscriber_information`;

-- ifnull(поле,вывод вместо null), вместо null ставим свое значение
select `comment_when_сonnecting`,
ifnull(`comment_when_сonnecting`,'здесь пусто') as where_is_null
from `data_set`.`subscriber_information`;
-- аналогичная конструкция через if:
select `comment_when_сonnecting`,
if(`comment_when_сonnecting` is null, 'здесь пусто', `comment_when_сonnecting`) as where_is_null
from `data_set`.`subscriber_information`;

-- оставляем только уникальные строки(distinct *) или ункикальнын записи в поле(distinct `col_name`)
-- select distinct * from `subscriber_information`;
select distinct `number_of_tv_devices` from `subscriber_information`;

--ГРУПИРОВКА GROUP BY
-- ЛИСТ 16,инициализируем оператор group by и перечисляем поля групировки c функцией агрегации подсчета кол-ва 0 и 1 по полю trust_payment,
-- а так-же делаем двойную сортировку по возврастанию, где родительская сортировка идет по полю connection_date,
-- а дочерняя сортировка по полю trust_payment
select `connection_date`,`trust_payment`,count(`trust_payment`)
from  `data_set`.`subscriber_information`
group by `connection_date`,`trust_payment`
order by `connection_date`,`trust_payment` asc

-- ЛИСТ 17, применяем агрегирующие функции count,max,min,avg,sum
-- with rollup итоги сводной
select `connection_date`,
count(`number_of_tv_devices`),
max(`number_of_tv_devices`),
min(`number_of_tv_devices`),
avg(`number_of_tv_devices`),
sum(`number_of_tv_devices`)
from  `data_set`.`subscriber_information`
group by `connection_date`
with rollup;

-- group_concat(), заспилтет через запятую все данные указаного поля в групировке
select `connection_date`,`trust_payment`,count(`trust_payment`),group_concat(`first_name`)
from  `data_set`.`subscriber_information`
group by `connection_date`,`trust_payment`
order by `connection_date`,`trust_payment` asc

-- having, фильтр, который работает так-же как и where, но только с полями сводной таблицы
select `connection_date`,`trust_payment`,count(`trust_payment`)
from  `data_set`.`subscriber_information`
group by `connection_date`,`trust_payment`
having  `trust_payment` = 1
order by `connection_date`,`trust_payment` asc

-- having, фильтр с использованием LIKE поля group_concat_first_name
select `connection_date`,`trust_payment`,count(`trust_payment`) as `count_trust_payment`,group_concat(`first_name`) as `group_concat_first_name`
from  `data_set`.`subscriber_information`
group by `connection_date`,`trust_payment`
having  `group_concat_first_name` like ('%Johnny%')
order by `connection_date`,`trust_payment` asc






