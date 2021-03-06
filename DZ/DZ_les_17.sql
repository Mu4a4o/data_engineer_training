subscriber_information.id_abon - PK
------------------------------------ДЕНИС-----------------------------
period_traffic.id_abon - PK(составной ключ) / FK(subscriber_information.id_abon)
period_traffic.day - PK (составной ключ)
------------------------------------ОЛЯ-------------------------------
house_info.id_abon - PK / FK(subscriber_information.id_abon)
------------------------------------МАКС------------------------------
abon_cities.id_abon - PK / FK(subscriber_information.id_abon)
----
states.city PK / FK(abon_cities.city)
------------------------------------СОФЬЯ-----------------------------
abon_podkl.id_abon FK(subscriber_information.id_abon)
abon_podkl.id_podkl PK
----
abon_spis.id_podkl PK / FK(abon_podkl.id_podkl)
----
abon_sales.id_podkl PK / FK(abon_podkl.id_podkl)



1. Написать триггер для subscriber_information
   Параметрами будут before insert
   Задача триггера добавлять текущую дату в поле comment_when_сonnecting при добавлении новых записей

2. Написать процедуру.
   Входящие атрибуты :
        id_abon,
        first_name,
        last_name,
        connection_date,
        trust_payment,
        number_of_internet_devices,
        number_of_tv_devices,
        comment_when_сonnecting
   Задача процедуры, добавить данные из входящих атрибутов в таблицу subscriber_information.

3. Написать триггеры для всех таблиц, которые имеют связь по FK с таблицей subscriber_information.
   Параметрами будут before insert
   Задача триггеров проверять поле id_abon или составных PK на предмет дублирующей записи. В случае подтверждения дубликата, выводить надпись
  "id_abon for X... already available" , где 'X...' номер id.

4. Создать таблицу(название ваше) с полями получеными в ходе выполнения задачи под номером восемь в DZ_les_16

5. Написать триггер для таблицы из предыдущей пункта задачи.
   Параметрами будут before insert
   Задача триггера проверять на предмет дублирующей строчки, т.е. всех полей . В случае подтверждения дубликата, выводить надпись
  "row already available" .

6. Написать процедуру.
   Без атрибутов.
   Задача процедуры, отрабатывать скрипт полученый в ходе выполнения задачи под номером восемь в DZ_les_16 и эти данные инсертить в таблицу,
   которую создали в четвертом пункте.








