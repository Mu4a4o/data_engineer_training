##
# Алгоритмы сортировки
# Оценка сложности алгоритмов, или Что такое О(log n)
'''
O(n) — линейная сложность
Такой сложностью обладает, например, алгоритм поиска наибольшего элемента в не отсортированном массиве.
Нам придётся пройтись по всем n элементам массива, чтобы понять, какой из них максимальный.

O(log n) — логарифмическая сложность
Простейший пример — бинарный поиск. Если массив отсортирован, мы можем проверить, есть ли в нём какое-то конкретное значение, методом деления пополам.
Проверим средний элемент, если он больше искомого, то отбросим вторую половину массива — там его точно нет.
Если же меньше, то наоборот — отбросим начальную половину. И так будем продолжать делить пополам, в итоге проверим log n элементов.

O(n2) — квадратичная сложность
Такую сложность имеет, например, алгоритм сортировки вставками.
В канонической реализации он представляет из себя два вложенных цикла: один, чтобы проходить по всему массиву, а второй, чтобы находить место очередному элементу в уже отсортированной части.
Таким образом, количество операций будет зависеть от размера массива как n * n, т. е. n2.
'''

## Пузырьковая сортировка
# Если взять самый худший случай (изначально список отсортирован по убыванию), затраты времени будут равны O(n²), где n — количество элементов списка.
import time
st = time.time()
spis = [2,4,7,8,5,6]
def bubble_sort_alg(spis):
    flg = True
    while flg:
        flg = False
        for i in range(len(spis) - 1):
            if spis[i] > spis[i+1]:
                spis[i],spis[i+1] = spis[i+1],spis[i]
                flg = True
    return spis

print(bubble_sort_alg(spis))
print("----%.10f----"%(time.time()-st))
## Сортировка выбором
# Затраты времени на сортировку выбором в среднем составляют O(n²), где n — количество элементов списка.
import time

st = time.time()
nums = [2,4,7,8,5,6]

def selection_sort_alg(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
               if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums


print(selection_sort_alg(nums))
print("----%.10f----"%(time.time()-st))

## Быстрая сортировка
# Затраты времени на сортировку выбором в среднем составляют O(n log n), где n — количество элементов списка.
##Алгоритмы
import time
import copy
import random
import pandas

# Максим
# сортировка выбором (Макс)
def selection_sort_alg_maks(nums):
    count = 0
    for i in range(len(nums) - 1):
        m = i
        j = i + 1
        while j < len(nums):
            count += 1
            if nums[j] < nums[m]:
                m = j
            j = j + 1
        nums[i], nums[m] = nums[m], nums[i]
    return count
    #return nums

# сортировка пузырьковая (Макс)
def bubble_sort_alg_maks(nums):
    count = 0
    for i in range (len(nums)-1):
        for j in range(len(nums)-1-i):
            count += 1
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return count
    #return nums

# Софья
# сортировка пузырьковая (Софья)
def bubble_sort_alg_sofya(nums):
    count = 0
    for j in range(len(nums)-1):
        for k in range(len(nums)-1):
            count += 1
            if nums[k] > nums[k+1]:
                nums[k], nums[k+1] = nums[k+1], nums[k]
    return count
    #return nums

# # сортировка выбором (Софья) способ 1
# def selection_sort_1_alg_sofya(nums):
#     p = 0
#     for j in range(len(nums)):
#         m = 1000
#         for i in range(p, len(nums)):
#             if nums[i] < m:
#                 m = nums[i]
#                 k = i
#         nums[k], nums[j] = nums[j], nums[k]
#         p = p + 1
#     return nums

# сортировка выбором (Софья) способ 2
def selection_sort_2_alg_sofya(nums):
    count = 0
    for i in range(len(nums)):
        k = i
        for j in range(i + 1, len(nums)):
            count += 1
            if nums[j] < nums[k]:
                k = j
        nums[k], nums[i] = nums[i], nums[k]
    return count
    #return nums



# сортировка пузырьком (Денис)
def bubble_sort_alg(spis):
    count = 0
    flg = True
    while flg:
        flg = False
        for i in range(len(spis) - 1):
            count += 1
            if spis[i] > spis[i+1]:
                spis[i],spis[i+1] = spis[i+1],spis[i]
                flg = True
    return count
    #return spis

# сортировка выбором (Денис)
def selection_sort_alg(nums):
    count = 0
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            count += 1
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return count
   #return nums

# быстрая сортировка (Денис)

def quick_sort_alg(val):
    global count_val
    if len(val) == 2:
        if val[0] > val[1]:
            count_val += 1
            return [val[1],val[0]]
        else:
            return val
    elif len(val) == 1:
        return val
    else:
        opr = val[round(len(val)/2)]
        sm = []
        op = []
        bg = []
        for i in val:
            count_val += 1
            if i < opr:
                sm.append(i)
            elif i == opr:
                op.append(i)
            else :
                bg.append(i)
        if not bg and sm:
            return quick_sort_alg(sm)+op
        if not sm and bg:
             return op + quick_sort_alg(bg)
        if not sm and not bg:
            return op

        return quick_sort_alg(sm)+op+quick_sort_alg(bg)


## сравниваем алгоритмы на 50 генераций
import pandas as pd

# словарь результатов
# number_list - идентификатор списка
# count_oper - кол-во циклов в алгоритме
# alg_type - тип алгоритма
# author - автор алгоритма
# res_len - кол-во элеметов в списке
# res_min - минимальное значение в списке
# res_max - максимальное значение в списке
# res_unique - уникальных чисел в списке
# time_alg - время сортироквки
result_alg = {"number_list":[],"count_oper":[],"alg_type":[],"author":[],"res_len":[],"res_min":[],"res_max":[],"res_unique":[],"time_alg":[]}
for i in range(500):

    res = [random.randrange(1, 50000, 1) for i in range(random.randrange(1, 5000, 1))]

    # создаем копии листа (на всякий случай!!!)
    python_list = copy.deepcopy(res)
    quicksort_list = copy.deepcopy(res)
    selection_list = copy.deepcopy(res)
    bubble_list = copy.deepcopy(res)
    bubble_list_maks = copy.deepcopy(res)
    bubble_list_sofya = copy.deepcopy(res)
    selection_list_maks = copy.deepcopy(res)
    #selection_list_1_sofya = copy.deepcopy(res)
    selection_list_2_sofya = copy.deepcopy(res)


    # сортировка питоновская
    st = time.time()
    sorted(python_list)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("python_sort")
    result_alg["author"].append("Python")
    result_alg["res_len"].append(len(python_list))
    result_alg["res_min"].append(min(python_list))
    result_alg["res_max"].append(max(python_list))
    result_alg["res_unique"].append(len(set(python_list)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(0)

    # быстрая сортировка (Ден)
    st = time.time()
    # используем глобальную переменную для подсета шагов (из-за реккурсии). Это плохая практика!!!
    count_val = 0
    quick_sort_alg(quicksort_list)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("quicksort_sort")
    result_alg["author"].append("Den")
    result_alg["res_len"].append(len(quicksort_list))
    result_alg["res_min"].append(min(quicksort_list))
    result_alg["res_max"].append(max(quicksort_list))
    result_alg["res_unique"].append(len(set(quicksort_list)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(count_val)

    # соритровка выбором (Ден)
    st = time.time()
    count = selection_sort_alg(selection_list)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("selection_sort")
    result_alg["author"].append("Den")
    result_alg["res_len"].append(len(selection_list))
    result_alg["res_min"].append(min(selection_list))
    result_alg["res_max"].append(max(selection_list))
    result_alg["res_unique"].append(len(set(selection_list)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(count)

    # соритровка пузырьком (Ден)
    st = time.time()
    count = bubble_sort_alg(bubble_list)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("bubble_sort")
    result_alg["author"].append("Den")
    result_alg["res_len"].append(len(bubble_list))
    result_alg["res_min"].append(min(bubble_list))
    result_alg["res_max"].append(max(bubble_list))
    result_alg["res_unique"].append(len(set(bubble_list)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(count)

    # соритровка пузырьком (Макс)
    st = time.time()
    count = bubble_sort_alg_maks(bubble_list_maks)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("bubble_sort")
    result_alg["author"].append("Maks")
    result_alg["res_len"].append(len(bubble_list_maks))
    result_alg["res_min"].append(min(bubble_list_maks))
    result_alg["res_max"].append(max(bubble_list_maks))
    result_alg["res_unique"].append(len(set(bubble_list_maks)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(count)

    # соритровка выбором (Макс)
    st = time.time()
    selection_sort_alg_maks(selection_list_maks)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("selection_sort")
    result_alg["author"].append("Maks")
    result_alg["res_len"].append(len(selection_list_maks))
    result_alg["res_min"].append(min(selection_list_maks))
    result_alg["res_max"].append(max(selection_list_maks))
    result_alg["res_unique"].append(len(set(selection_list_maks)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(count)

    # соритровка пузырьком (Софья)
    st = time.time()
    bubble_sort_alg_sofya(bubble_list_sofya)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("bubble_sort")
    result_alg["author"].append("Sofya")
    result_alg["res_len"].append(len(bubble_list_sofya))
    result_alg["res_min"].append(min(bubble_list_sofya))
    result_alg["res_max"].append(max(bubble_list_sofya))
    result_alg["res_unique"].append(len(set(bubble_list_sofya)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(count)

    # # соритровка выбором (Софья) вариант 1
    # st = time.time()
    # print(selection_sort_1_alg_sofya(selection_list_1_sofya)[0:10])
    # result_alg["time_alg"].append(float("%.7f"%(time.time()-st)))
    # result_alg["alg_type"].append("selection_sort_1")
    # result_alg["author"].append("Sofya")

    # соритровка выбором (Софья) вариант 1
    st = time.time()
    selection_sort_2_alg_sofya(selection_list_2_sofya)
    result_alg["time_alg"].append(float("%.9f"%(time.time()-st)))
    result_alg["alg_type"].append("selection_sort_2")
    result_alg["author"].append("Sofya")
    result_alg["res_len"].append(len(selection_list_2_sofya))
    result_alg["res_min"].append(min(selection_list_2_sofya))
    result_alg["res_max"].append(max(selection_list_2_sofya))
    result_alg["res_unique"].append(len(set(selection_list_2_sofya)))
    result_alg["number_list"].append(i+1)
    result_alg["count_oper"].append(count)

#print(result_alg)
df = pd.DataFrame(result_alg)
#print(df.head(n=100))
path = "/test.xlsx"
df.to_excel(path,index = False,sheet_name="test")


