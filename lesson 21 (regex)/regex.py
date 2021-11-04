'''
% - произвольное кол-во символов
lesson 24 (python,excel) - любой одиночный символ
$ - конец строки
^ - начало строки
[ ] - любой из них или диапазоны
*/
-- https://regex101.com/
https://dev.mysql.com/doc/refman/8.0/en/regexp.html#operator_regexp

-- Примеры на SQL
-- Маска это свойства регуляного выражения состоящий из метасимволов и самих символов, которые позволяют обеспечить нужный вывод данных
-- маска с метасимволом '%' обозначает вывод любых символов произвольного кол-ва
-- Пример с оператором LIKE, где 'W%' выводит все слова,которые начинаются с WA...
select distinct first_name from  subscriber_information_big where first_name LIKE 'WA%';
-- Пример с оператором LIKE, где '%W' выводит все слова,которые заканчиаваются на ...W
select distinct first_name from  subscriber_information_big where first_name LIKE '%W';
-- Пример с оператором LIKE, где '%W%' выводит все слова,которые имеют букву W в любом месте
select distinct first_name from  subscriber_information_big where first_name LIKE '%W%';
-- маска с метасимволом 'lesson 24 (python,excel)' обозначает вывод любого,одного символа
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
'''

## Примеры на Pandas
import pandas as pd

#Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
'''
https://habr.com/ru/post/349860/
\ - экранирование
\d - любую цифру
\D - все что угодно, кроме цифр
\s - пробелы
\S - все кроме пробелов
\w - буква или цифра
\W - все кроме букв или цифр
\b - граница слова
\B - не границ
{2}- повторение два раза
'''

path_file = '/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 20 (pandas,generation)/big_si.csv'
# открываем файл с явными типами
df_si = pd.read_csv(path_file,
                    sep=';',
                    header=None,
                    dtype=
                            {
                                0: 'object',
                                1: 'category',
                                2: 'category',
                                4: 'int8',
                                5: 'int8',
                                6: 'int8',
                                7: 'category',
                            })

print(df_si.info(memory_usage='deep'))

name_columns = ['id_abon', 'first_name', 'last_name', 'connection_date', 'trust_payment', 'number_of_internet_devices',
                'number_of_tv_devices', 'comment_when_сonnecting']
df_si.columns = name_columns

# Форматируем в дату
df_si['connection_date'] = pd.to_datetime(df_si['connection_date'], format='%Y-%m-%d')
print(df_si.info(memory_usage='deep'))

# В отличии от SQL чувстителен к регистру !!!

##Пример поиск подстроки состоящих из символов 'W|S' в указаном порядке, где метасимвол '|' обозначает 'или'
df_si[df_si['first_name'].str.contains('[a|S]', regex= True, na=False)]

## Пример поиск подстроки состоящих из символов '^Wi' в указаном порядке, где метасимвол '^' (циркуфлекс,крышка) обозначает начало строки
df_si[df_si['first_name'].str.contains('^Wi', regex= True, na=False)]

## Пример поиск подстроки состоящих из символов 'at$' в указаном порядке, где метасимвол '$' обозначает конец строки
df_si[df_si['first_name'].str.contains('at$', regex= True, na=False)]

## Пример поиск подстроки состоящих из символов '\d\d\d\d\d\d\D\D-\d' в указаном порядке,
# где метасимвол '\d' обозначает любая цифра,
# а метасимвол '\D' обозначает любая НЕ цифра,
df_si[df_si['id_abon'].str.contains('\d\d\d\d\d\d\D\D-\d', regex= True, na=False)]

## Пример поиск подстроки состоящих из символов '\W\d\d[a-zA-Z]' в указаном порядке,
# где метасимвол '\W' обозначает все кроме букв или цифр,
# '\d' обозначает любая цифра,
# '[a-zA-Z]' обозначает любая буква,
# '{2}' повторение два раза
df_si[df_si['id_abon'].str.contains('\W\d\d[a-zA-Z]\d\W', regex= True, na=False)]
#df_si[df_si['id_abon'].str.contains('\W\d{2}[a-zA-Z]\d\W', regex= True, na=False)]

## Поиск и замена с помощью regex
df_si['id_abon_3'] = df_si['id_abon'].str.replace('\W', '', regex=True)
print(df_si)

