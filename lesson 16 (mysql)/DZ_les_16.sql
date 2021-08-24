1.  Сджойнить (LJ) таблицы (abon_cities,abon_podkl,abon_sales,abon_spis,house_info,
    period_traffic,states,subscriber_information), где `subscriber_information` будет основная и вывести уникальные поля.

2.  Вывести subscriber_information.id_abon и states.state.
    Условием вывода будут те, чей abon_podkl.date_podkl равен январю 2020 года.

3.  Сделать 1 пункт и к нему привязать условие из 2 пункта.

4.  Вывести house_info.id_house, states.state, abon_sales.sale.
    Условием вывода будут те, чей abon_spis.tarif_after равен 'Все включено v.3.5'

5.  Вывести subscriber_information.id_abon, subscriber_information.number_of_internet_devices, subscriber_information.number_of_tv_devices
    Условием вывода будут те,кто был от 01.02.20(вкл) поля abon_sales.date_start_sale и до 2020-04-01(вкл) поля abon_sales.date_end_sale
    Сделать двойную сортировку по возрастанию,сначала abon_sales.date_start_sale потом abon_sales.date_end_sale.

6.  Вывести subscriber_information.connection_date, subscriber_information.number_of_internet_devices,
    subscriber_information.number_of_tv_devices,а так-же previous_number_internet и previous_number_tv.
    Поле previous_number_internet - это предыдущее значение поля subscriber_information.number_of_internet_devices
    Поле previous_number_tv - это предыдущее значение поля subscriber_information.number_of_tv_devices
    Партиционирование оконной функции этих полей происходит по subscriber_information.connection_date,
    а оконная сортировка по subscriber_information.id_abon.

7.  !!!К таблице 6 пункта добавить поля abon_cities.city,abon_cities.state, а так-же count_abon_city и count_abon_state
    Поле count_abon_city - это кол-во пользователей проживающий в этом городе.
    Поле count_abon_state - это кол-во пользователей проживающий в этом штате.!!!

8.  !!!К таблице 7 пункта добавить поле total_traffic_id_abon.
    Поле total_traffic_id_abon - это сумарный трафик за все время, который высчитывется по полю period_traffic.traffic_gb!!!






