import sys
import time
def DZ_decor(DZ_func):
    file = 'C:/Users/SoVYakovleva/Desktop/Python_lessons/log.txt'
    def the_wrapper_around_the_original_function(*args):
        try:
            sys.stdout = open(file, 'a')
            first_time = time.time()
            print('Текущее время first_time', first_time)
            k = DZ_func(*args)
            print('Время выполнения перемножения:', time.time() - first_time)
            print(6/0)
            return k
        except Exception as ex:
            sys.stderr = open(file, 'a')
            first_time = time.time()
            print(ex, 'Текущее время first_time', first_time)
            k = DZ_func(*args)
            print('Время выполнения перемножения:', time.time() - first_time)
            return k
            sys.stderr.close()
        finally:
            sys.stdout.close()
    return the_wrapper_around_the_original_function

@DZ_decor
def DZ_funk(*args):
    a = 1
    b = 0
    for i in range(len(args)):
        if args[i] == 1:
            b = b + 1
        else:
            if type(args[i]) != int:
                print('Значение аргумента ', i+1, 'не числовое, тип этого аргумента: ', type(args[i]))
            else:
                a = a*args[i]
    print('Произведение числовых аргументов : ', a)
    if a == 1 and b == 0:
        print('Произведение числовых аргументов указано по умолчанию, числовых аргументов нет выберите другие')
    time.sleep(3)
    return a

DZ_funk(7,3,1,7)
