
-- Оконная функция
-- Подсчет кол-ва дат в отельном поле
-- Агрегирующая функция (COUNT) партиционирование по полю ( PARTITION BY )
SELECT
`connection_date`,
COUNT(`connection_date`) OVER (PARTITION BY `connection_date`) as `count_date`
FROM
`subscriber_information`

-- Использование функции ROW_NUMBER для нумерации дат по их партициоинированию.
-- Делаем двойную соритровку
SELECT
`connection_date`,
row_number() OVER (PARTITION BY `connection_date` ) as `row_number_date`
FROM
`subscriber_information`
ORDER BY `connection_date`,`row_number_date`

-- выводим следующую строку при помощи функции LEAD
SELECT
`id_abon`,
`connection_date`,
LEAD(`connection_date`,1) OVER (ORDER BY  `id_abon`) as `lead_date`
FROM
`subscriber_information`

-- выводим предыдущую строку  при помощи функции   LAG
SELECT
`id_abon`,
`connection_date`,
LAG(`connection_date`,1) OVER (ORDER BY  `id_abon`) as `lead_date`
FROM
`subscriber_information`

-- выводим только нужжные строки , которые есть в другой таблице при помощи EXIST
SELECT *
FROM `subscriber_information`
 WHERE EXISTS
  (SELECT *
     FROM  `subscriber_information`
    WHERE  `subscriber_information`.`id_abon` = `subscriber_information`.`id_abon`);


-- функция COALESCE проверяет ячейку на null. В противном случае возращает заглушку
SELECT `t1`.*
,coalesce(`t2`.`day`,'1900-01-01') as `day`
,coalesce(`t2`.`traffic_gb`,0) as `traffic_gb`
FROM `subscriber_information_join` as `t1`
LEFT JOIN `period_traffic_join` as `t2` ON `t1`.`id_abon` = `t2`.`id_abon`


-- фильтры при джойне или основной фильтр
SELECT *
FROM `subscriber_information` as `t1`
LEFT JOIN `period_traffic` as `t2` ON `t1`.`id_abon` = `t2`.`id_abon`
WHERE  `traffic_gb` > 400*/

SELECT *
FROM `subscriber_information` as `t1`
LEFT JOIN `period_traffic` as `t2` ON `t1`.`id_abon` = `t2`.`id_abon`
AND  `t2`.`traffic_gb` > 400

-- Sofia

-- one level join

 select `si`.*,`ap`.*
 from `subscriber_information` as `si`
 left join `abon_podkl` as `ap` on `ap`.`id_abon` = `si`.`id_abon`
 order by `si`.`id_abon`;

-- one and two level join

 select `si`.*,`ap`.*,`asa`.*,`asp`.*
 from `subscriber_information` as `si`
 left join `abon_podkl` as `ap` on `ap`.`id_abon` = `si`.`id_abon`
 left join `abon_sales` as `asa` on `asa`.`id_podkl` = `ap`.`id_podkl`
 left join `abon_spis` as `asp` on `asp`.`id_podkl` = `ap`.`id_podkl`
 order by `si`.`id_abon`;

-- Maks

-- one level join

 select `si`.*,`ac`.*
 from `subscriber_information` as `si`
 left join `abon_cities` as `ac` on `ac`.`c_abon` = `si`.`id_abon`
 order by `si`.`id_abon`;


-- two level join

 select `si`.*,`ac`.*,`st`.*
 from `subscriber_information` as `si`
 left join `abon_cities` as `ac` on `ac`.`c_abon` = `si`.`id_abon`
 left join `states` as `st` on `st`.`s_city` = `ac`.`city`
 order by `si`.`id_abon`;


-- general Sofya + Maks and USING

 select `si`.*,`ap`.* ,`asa`.*,`asp`.*,`ac`.*,`st`.*
 from `subscriber_information`  as `si`
 left join `abon_podkl` as `ap` USING (`id_abon`)
 left join `abon_sales` as `asa` USING (`id_podkl`)
 left join `abon_spis` as `asp` USING (`id_podkl`)
 left join `abon_cities` as `ac` on `ac`.`c_abon` = `si`.`id_abon`
 left join `states` as `st` on `st`.`s_city` = `ac`.`city`
 order by `si`.`id_abon`;