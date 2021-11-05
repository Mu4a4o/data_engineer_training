
--  устанавливаем DOCKER INSTALLER
docker desktop installer

-- Скачаваем образ docker с последней версией mysql и запускаем контейнер 'mysql_instance'
docker run --name mysql_instance -e MYSQL_ROOT_PASSWORD=mu4a4o212 -e LANG=C.UTF-8 -p 3308:3306 -d mysql/mysql-server:latest
-- подключаемся к серверу mysql
docker exec -it mysql_instance mysql -uroot -pmu4a4o212
-- создаем локального юзера 'den' и задаем пароль
CREATE USER 'den'@'localhost' IDENTIFIED BY 'mu4a4o313';
-- назначаем ему косммические права
GRANT ALL PRIVILEGES ON *.* TO 'den'@'localhost' WITH GRANT OPTION;
-- создаем внешнего юзера 'den' и задаем пароль
CREATE USER 'den'@'%' IDENTIFIED BY 'mu4a4o313';
-- назначаем ему косммические права
GRANT ALL PRIVILEGES ON *.* TO 'den'@'%' WITH GRANT OPTION;
-- применяем настройки выше
FLUSH PRIVILEGES;
exit

-- посмотреть запущенные контейнеры
docker container ls
--  остановить работу контейнера
docker stop mysql_instance
--  запустить работу контейнера
docker start mysql_instance
docker run --name=mysql_instance -p 3305:3306 mysql

-- сохранить образ контейенера и переместить
1. запускаем на контейнер
2. docker ps (копируем CONTAINER ID)
3. docker commit "CONTAINER ID" "NAME IMAGE"
(коммитим в образ и не забываем вставить "CONTAINER ID" из 2 пункта + "NAME IMAGE" название образа)
4. docker save "NAME IMAGE" > "name_file.tar" (сохраняем файл образа)
5. "name_file.tar" (файл образа) переносим на другой сервер
6. docker load < "name_file.tar" (загружаем образ в другой докер)
7. docker run --name mysql_instance -e MYSQL_ROOT_PASSWORD=mu4a4o212 -e LANG=C.UTF-8 -p 3308:3306 -d "NAME IMAGE"





