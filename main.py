def first_lesson():
    print('произведение')
    a = 5 * 5
    print('5 * 5 =', a, '\n')

    print('частное')
    a = 5 // 5
    print('5 / 5 =', a, '\n')

    print('разность')
    a = 5 - 5
    print('5 - 5 =', a, '\n')

    print('сумма')
    a = 5 + 5
    print('5 + 5 =', a, '\n')

    print('возведение в степень')
    a = 2 ** 3
    print('2 ** 3 = ', a, '\n')

    print('остаток от деления')
    a = 5 % 3
    b = 5 % 5
    print('5 % 3 = ', a)
    print('5 % 5 = ', b)
    print('____________________________________', '\n')

    print('ПЕРЕМЕННЫЕ', '\n')

    print('ИЗМЕНЯЕМЫЕ ТИПЫ')

    type_list = [1, '2', 3.0]
    print('тип лист', type(type_list), type_list)

    type_dict = {1: 'one', 'two': 2, 3.0: 3}
    print('тип словарь', type(type_dict), type_dict)

    type_set = {1, '2', 3.0, 3.0}
    print('тип множества (не индексируемый, неупорядоченны, не имеет дубликатов', type(type_set), type_set)


if __name__ == '__main__':
    first_lesson()

