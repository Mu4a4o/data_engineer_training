# Выделить почты с доменами  @index.ru @yandex.ru

## Денис ##
import re
reg_DEN = r'[a-zA-Z0-9]*@index.ru|[a-zA-Z0-9]*@yandex.ru'

mail = open(r'/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 21 (regex)/email').readline()
match = re.findall(reg_DEN, mail)
print(match)


