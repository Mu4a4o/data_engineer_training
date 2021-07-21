-- ВЫБОР (SELECT)
--ЛИСТ 1 выбор всех записей(*)
select * from 'table_name';

--ЛИСТ 2 выбор определенных колонок,перечисление колонок через запятую
select 'col_name_1','col_name_2' from 'table_name';

--ВЫБОР С УСЛОВИЕМ (WHERE)
--ЛИСТ 3 условие, больше(>) 0  и(and) меньше(<) 5 и(and) не равно(<> и !=) 3
select * from 'table_name' where 'col_1' > 0 and 'col_1' < 5 and 'col_1' <> 3;

--ЛИСТ 4 условия, равно(=) 3 ИЛИ(or) равно(=) 2
select * from 'table_name' where 'col_1'= 7  or 'col_1' = 8;

--ЛИСТ 5 условие, только не пустое(id not null)
select * from 'table_name' where  'col_2 ' is not null;

--ЛИСТ 6 условие, только пустые(is null)
select * from 'table_name' where 'col_2' is null;


