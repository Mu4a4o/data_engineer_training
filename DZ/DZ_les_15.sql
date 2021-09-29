-- subscriber_information (id_abon PK)
-- subscriber_information.connection_date - когда был подключен абоненент
-- subscriber_information.comment_when_сonnecting - довольный/недовольный/нейтральный комментарий абонента при подключении
-- subscriber_information.number_of_tv_devices - кол-во установленных ТВ устройств при подключении
-- subscriber_information.number_of_internet_devices - кол-во установленных  ИНТЕРНЕТ устройств при подключении

-- period_traffic (id_abon PK FK --> subscriber_information.id_abon),day PK)
-- period_traffic.day - дата трафика
-- period_traffic.traffic_gb - трафик абонентов

1.1 Вывести все поля по subscriber_information.
1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)
1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)
1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices
1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.

2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!
2.2 Сделать LJ subscriber_information(основная) и period_traffic.
	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
    В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).
2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.
2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении,
    а так-же были подключены ранее 2020-01-15, и чей трафик был
	в промежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) и не более 100 GB. !!!



    

