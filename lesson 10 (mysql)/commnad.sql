

-- меняем пароль
alter user 'root'@'localhost' IDENTIFIED by 'MyPassword';
--  применяем значения
flush privileges;

-- создаем БД
create database data_engineer;

--смотрим БД
show databases;

-- активируем БД
use data_engineer;

-- смотрим список таблиц
show tables;

-- создаем таблицу c юзерами
create table data_engineer.user_info
(number INT NOT NULL AUTO_INCREMENT,
id INT UNIQUE,
name VARCHAR(255),
email VARCHAR(255),
date_create date,
CONSTRAINT id_pk PRIMARY KEY (number)
);

-- создаем таблицу связку с атрибутами
CREATE table data_engineer.user_attribute
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    attribute_id INT,
    created_at Date,
    FOREIGN KEY (attribute_id)  REFERENCES user_info (id)
);

-- создаем  таблицу с указанием атрибутов
CREATE table data_engineer.attribute
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    attribute varchar(255),
    FOREIGN KEY (id)  REFERENCES user_attribute (id)
);

-- смотрим список таблиц
show tables

--смотрим связи на схеме
WORKBENCH - DATABASES - REVERSE ENGINEER


-- снимаем дамп схемы БД без данных
WORKBENCH - SERVER - DATA EXPORT

-- генерируем данные
http://filldb.info
вставляем create table из дампа
генерируем БД по 1.jpg,2.jpg,3.jpg
export в beta
открываем запрос в WORKBENCH и применяем



-- вставляем данные с юзерами
insert into data_engineer.user_info (id,name,email,date_create)
values (3436,'Denis','3com@list.ru','2021-07-06'),
(3059,'Olya','olya@list.ru','2021-07-06'),
(7878,'Maks','maks@list.ru','2021-07-06'),
(67878,'Sofia','sofia@list.ru','2021-07-06')

-- вставляем данные в таблицу связки
insert into data_engineer.user_attribute (attribute_id,created_at)
values (3436,'2021-07-06'), (3059,'2021-07-06'), (7878,'2021-07-06'), (67878,'2021-07-06')

-- вставляем данные в таблицу атрибутов
insert into data_engineer.attribute (attribute)
values ('red'), ('red'), ('green'), ('white')

-- Просмотр структуры таблицы
DESCRIBE data_engineer.user_info





-- DML – Data Manipulation Language (язык манипулирования данными)
/*
SELECT – выборка данных
INSERT – вставка новых данных
UPDATE – обновление данных
DELETE – удаление данных
MERGE – слияние данных
*/

-- DDL – Data Definition Language (язык описания данных)
/*
CREATE – создание объектов
ALTER – изменение объектов
DROP – удаление объектов
*/







-- Встроеные функции и математические операции
-- Остаток от деления
select 9 % 4
select 9 % 3
-- Деление по модулю
select 9 DIV 4





