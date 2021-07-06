-- меняем пароль
alter user 'root'@'localhost' IDENTIFIED by 'MyPassword';
--  применяем значения
flush privileges;

-- создаем БД
create database data_engineer

--смотрим БД
show databases

-- активируем БД
use data_engineer

-- смотрим список таблиц
show tables

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

-- вставляем данные с юзерами
insert into data_engineer.user_info (id,name,email,date_create)
values (343,'Denis','3com@list.ru','2021-07-06'),
(3059,'Olya','olya@list.ru','2021-07-06'),
(7878,'Maks','maks@list.ru','2021-07-06'),
(67878,'Sofia','sofia@list.ru','2021-07-06')

-- вставляем данные в таблицу связки
insert into data_engineer.user_attribute (attribute_id,created_at)
values (343,'2021-07-06'), (3059,'2021-07-06'), (7878,'2021-07-06'), (67878,'2021-07-06')

-- вставляем данные в таблицу атрибутов
insert into data_engineer.attribute (attribute)
values ('red'), ('red'), ('green'), ('white')

-- DDL







