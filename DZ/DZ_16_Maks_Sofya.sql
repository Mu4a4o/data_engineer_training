-- ДЕНИС --
-- ПОЛЯ
-- 1.  Сджойнить (LJ) таблицы (abon_cities,abon_podkl,abon_sales,abon_spis,house_info,
--   period_traffic,states), где `subscriber_information` будет основная и вывести уникальные поля.
select
*
from subscriber_information as si
left join abon_cities ac using(id_abon)
left join abon_podkl ap using(id_abon)
left join abon_sales absl using(id_podkl)
left join abon_spis abs using(id_podkl)
left join house_info hi using(id_abon)
left join period_traffic pt using(id_abon)
left join states st using(city);

-- 2.  Вывести subscriber_information.id_abon и states.state.
--     Условие вывода -   abon_podkl.date_podkl равен январю 2020 года.
select
si.id_abon
,st.state
from subscriber_information as si
left join abon_podkl ap using(id_abon)
left join abon_cities ac using(id_abon)
left join states st using(city)
where 1=1
	and month(ap.date_podkl) = '01'
    and year(ap.date_podkl) = '2020';
-- 3.  Сделать 1 пункт и к нему привязать условие из 2 пункта.
select
*
from subscriber_information as si
left join abon_cities ac using(id_abon)
left join abon_podkl ap using(id_abon)
left join abon_sales absl using(id_podkl)
left join abon_spis abs using(id_podkl)
left join house_info hi using(id_abon)
left join period_traffic pt using(id_abon)
left join states st using(city)
where 1=1
	and month(ap.date_podkl) = '01'
    and year(ap.date_podkl) = '2020';

-- 4.  Вывести house_info.id_house, states.state, abon_sales.sale.
--     Условие вывода -  abon_spis.tarif_after равен 'Все включено v.3.5'
select
hi.id_house
,st.state
,absl.sale
from subscriber_information as si
left join abon_podkl ap using(id_abon)
left join abon_sales absl using(id_podkl)
left join abon_spis abs using(id_podkl)
left join house_info hi using(id_abon)
left join abon_cities ac using(id_abon)
left join states st using(city)
where 1=1
	and abs.tarif_after = 'Все включено v.3.5';
-- 5.  Вывести subscriber_information.id_abon, subscriber_information.number_of_internet_devices, subscriber_information.number_of_tv_devices
--     Условие вывода - abon_sales.date_start_sale от 01.02.20(вкл)  и abon_sales.date_end_sale до 2020-04-01(вкл)
--     Сделать двойную сортировку по возрастанию,сначала abon_sales.date_start_sale потом abon_sales.date_end_sale.
select
si.id_abon
,si.number_of_internet_devices
,si.number_of_tv_devices
-- ,absl.date_start_sale
-- ,absl.date_end_sale
from subscriber_information as si
left join abon_podkl ap using(id_abon)
left join abon_sales absl using(id_podkl)
	where 1=1
    and absl.date_start_sale >= '2020-02-01'
    and absl.date_end_sale <= '2020-04-01'
    order by absl.date_start_sale,absl.date_end_sale;

-- 6.  Вывести subscriber_information.connection_date, subscriber_information.number_of_internet_devices,
--     subscriber_information.number_of_tv_devices,а так-же previous_number_internet и previous_number_tv.
--     Поле previous_number_internet - это предыдущее значение поля subscriber_information.number_of_internet_devices
--     Поле previous_number_tv - это предыдущее значение поля subscriber_information.number_of_tv_devices
--     Партиционирование оконной функции этих полей происходит по subscriber_information.connection_date,
--     а оконная сортировка по subscriber_information.id_abon.
select
si.connection_date
,si.number_of_internet_devices
,si.number_of_tv_devices
,lag(si.number_of_internet_devices) over (partition by si.connection_date order by si.id_abon) previous_number_internet
,lag(si.number_of_tv_devices) over (partition by si.connection_date order by si.id_abon) previous_number_tv
from subscriber_information as si;

-- 7.  !!!К таблице 6 пункта добавить поля abon_cities.city,abon_cities.state, а так-же count_abon_city и count_abon_state
--    Поле count_abon_city - это кол-во пользователей проживающий в этом городе.
--     Поле count_abon_state - это кол-во пользователей проживающий в этом штате.!!!
select
si.connection_date
,si.number_of_internet_devices
,si.number_of_tv_devices
,lag(si.number_of_internet_devices) over (partition by si.connection_date order by si.id_abon) previous_number_internet
,lag(si.number_of_tv_devices) over (partition by si.connection_date order by si.id_abon) previous_number_tv
,ac.city
,st.state
,count(si.id_abon) over (partition by ac.city) count_abon_city
,count(si.id_abon) over (partition by st.state) ccount_abon_state
from subscriber_information as si
left join abon_cities ac using(id_abon)
left join states st using(city);
-- 8.  !!!К таблице 7 пункта добавить поле total_traffic_id_abon.
--     Поле total_traffic_id_abon - это сумарный трафик за все время, который высчитывется по полю period_traffic.traffic_gb!!!
select
si.id_abon
,si.connection_date
,si.number_of_internet_devices
,si.number_of_tv_devices
,lag(si.number_of_internet_devices) over (partition by si.connection_date order by si.id_abon) previous_number_internet
,lag(si.number_of_tv_devices) over (partition by si.connection_date order by si.id_abon) previous_number_tv
,ac.city
,st.state
,count(si.id_abon) over (partition by ac.city) count_abon_city
,count(si.id_abon) over (partition by st.state) ccount_abon_state
,sum(pt.traffic_gb) total_traffic_id_abon
from subscriber_information as si
left join abon_cities ac using(id_abon)
left join states st using(city)
left join period_traffic pt using(id_abon)
group by si.id_abon;