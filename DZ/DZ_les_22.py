# Выделить почты с доменами  @index.ru @yandex.ru

## Денис ##
import re
reg_DEN = r'[a-zA-Z0-9]*@index.ru|[a-zA-Z0-9]*@yandex.ru'
reg_DEN_2 = r'(?<=ru)[a-zA-Z0-9]*@yandex.ru|(?<=com)[a-zA-Z0-9]*@yandex.ru|(?<=ru)[a-zA-Z0-9]*@index.ru'

mail = open(r'/lesson 21 (regex)/email').readline()
mail_2 = 'ascasdf@cadsc.rusxas@cds.ruas@index.ruo@outlook.comhr6zdl@yandex.rukaft93x@outlook.comdcu@yandex.ru19dn@outlook.compa5h@mail.ru281av0@gmail.com8edmfh@outlook.comsfn13i@mail.rug0orc3x1@outlook.comrv7bp@gmail.com93@outlook.comer@gmail.como0my@gmail.com715qy08@gmail.comvubx0t@mail.ruwnhborq@outlook.comgq@yandex.ruic0pu@outlook.como7khr@yandex.ru2shlaq@outlook.comcdbw@yandex.ruwrts90puk@yandex.ruyxunv@gmail.com7y@yandex.ru6@mail.ruk8sjebg1y@mail.rujirbold@gmail.comu7yhwf1vb@mail.ruf@outlook.comgjkhp@mail.ruwyalkxfde@gmail.comf245n@outlook.comw@outlook.comjs3kyopz@mail.ruo@outlook.comuzfd@mail.rug@mail.rudvjf0@gmail.comd2mc@outlook.com06lk@mail.ruemhzysf2@yandex.rud1w28lkg@yandex.rut93@mail.rut3i@outlook.comt6ro3@gmail.com1zqnk0y7@yandex.ru768ptl4nv@gmail.combzq3yh2c1@mail.ru78k3dvwx@outlook.comfe8obp@mail.rucxh2daw8@outlook.comlrsdy5p@yandex.ru2de17h@mail.ruwe3l08z5@gmail.comi8ovxn2f@gmail.comq4as80@outlook.comopu@outlook.com5iar3l8k@yandex.ru4zegxla@mail.ru8lf0g@yandex.ru1zx8@yandex.rux@mail.ru34d@gmail.compxacl@mail.ru7o1@gmail.com1@gmail.comiut@gmail.come3t@outlook.com41clb6o2g@yandex.ru5hsbm8pi3@mail.rudihf8jxk@gmail.comdwej@yandex.ruzyue8brv@outlook.com0a5437@mail.rufovtju3q2@yandex.ru5ntglejc9@outlook.com61rpbj@mail.ru9m6pfk52r@outlook.comgr@yandex.ruv9dux@gmail.commek975vcx@gmail.comuakvj8p9d@yandex.rut3m6u8v@gmail.comjxqme@gmail.comc3@gmail.com3xkgmsd9t@gmail.coms9iw@mail.ruqo2sc@mail.ruxiuq5olft@gmail.com8swlo27hd@outlook.comr0o6f92@gmail.comz@gmail.comr3p4mgf5@yandex.rup@outlook.com61j@yandex.rut2sr@gmail.comu7@outlook.com9k15qr2h@gmail.com3vmtdo1@outlook.comq9@mail.ru'
match = re.findall(reg_DEN, mail)
print(match)

match_2 = re.findall(reg_DEN_2, mail_2)
print(match_2)

