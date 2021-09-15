/*
% - произвольное кол-во символов
_ - любой одиночный символ
$ - конец строки
^ - начало строки
[ ] - любой из них или диапазоны
*/
-- https://regex101.com/

-- Маска это свойства регуляного выражения состоящий из метасимволов и самих символов, которые позволяют обеспечить нужный вывод данных
-- маска с метасимволом '%' обозначает вывод любых символов произвольного кол-ва
-- Пример с оператором LIKE, где 'W%' выводит все слова,которые начинаются с WA...
select distinct first_name from  subscriber_information_big where first_name LIKE 'WA%';
-- Пример с оператором LIKE, где '%W' выводит все слова,которые заканчиаваются на ...W
select distinct first_name from  subscriber_information_big where first_name LIKE '%W';
-- Пример с оператором LIKE, где '%W%' выводит все слова,которые имеют букву W в любом месте
select distinct first_name from  subscriber_information_big where first_name LIKE '%W%';
-- маска с метасимволом '_' обозначает вывод любого,одного символа
-- Пример с оператором LIKE, где '_W_' выводит все слова,которые имеют букву W окруженная символами слева и справа от себя .W.
select distinct first_name from  subscriber_information_big where first_name LIKE '_W_';
-- Пример с оператором LIKE, где '%W_' с двойными метасимволами. Выводит все знаки до W и один после ...W.
select distinct first_name from  subscriber_information_big where first_name LIKE '%W_';


-- Оператор regexp. Полноценная реализация регулярных выражений
-- Пример поиск подстроки состоящих из символов 'AT' в указаном порядке
select distinct first_name from  subscriber_information_big where first_name REGEXP 'AT';
-- Пример поиск подстроки состоящих из символов '^AT' в указаном порядке, где метасимвол '^' (циркуфлекс,крышка) обозначает начало строки
select distinct first_name from  subscriber_information_big where first_name REGEXP '^AT';
-- Пример поиск подстроки состоящих из символов 'AT$' в указаном порядке, где метасимвол '$' обозначает конец строки
select distinct first_name from  subscriber_information_big where first_name REGEXP 'AT$';
-- Пример поиск подстроки состоящих из символов 'AT|BP' в указаном порядке, где метасимвол '|' обозначает 'или'
select distinct first_name from  subscriber_information_big where first_name REGEXP 'BI|BA';
-- Пример поиск подстроки состоящих из символов 'H[OA]' в указаном порядке, где метасимвол '[]' обозначает любой символ в скобках после H
select distinct first_name from  subscriber_information_big where first_name REGEXP 'H[OA]';
-- Пример поиск подстроки состоящих из символов 'H[OA]T' в указаном порядке, где метасимвол '[]' обозначает любой символов в скобках после H и перед T
select distinct first_name from  subscriber_information_big where first_name REGEXP 'H[OA]T';
-- Пример поиск подстроки состоящих из символов 'H[A-E]' в указаном порядке, где метасимвол '[-]' обозначает любой символ от A до E в скобках после H
select distinct first_name from  subscriber_information_big where first_name REGEXP 'H[A-E]';
-- Пример поиск подстроки состоящих из символов 'H[A-E]' в указаном порядке, где метасимвол '[-]' обозначает любой символ от A до E в скобках после H
select distinct first_name from  subscriber_information_big where first_name REGEXP 'H[A-E]';

-- Далее примеры на https://regex101.com/ где будем использовать остальные метасимволы
/*
\ - экранирование
\d - любую цифру
\D - все что угодно, кроме цифр
\s - пробелы
\S - все кроме пробелов
\w - буква
\W - все кроме букв
\b - граница слова
\B - не границ
*/
select id_abon from subscriber_information_big;