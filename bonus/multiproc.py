# import datetime
# from multiprocessing import Pool
#
# def sum_num (val):
#     k = 0
#     for l in range(100):
#         for i in val:
#             k = k + i
#     return k
#
#
#
# num_list = np.array([random.randrange(0,10) for i in range(0,9999999)])
# print('end_gener_one')
#
# a = datetime.datetime.now()
# print(sum_num(num_list))
# print(datetime.datetime.now() - a)
# print('end_one_proc')
#
# a = datetime.datetime.now()
# p = Pool(processes = 16)
# print(sum(p.map(sum_num,np.array_split(num_list,16))))
# print(datetime.datetime.now() - a)
# print('end_multy_proc')
import random
import copy
import functools
from multiprocessing import Process,Value,Array,Pool

# сортировка пузырьковая (Макс)
def bubble_sort_alg_maks(nums):
    count = 0
    for i in range (len(nums)-1):
        for j in range(len(nums)-1-i):
            count += 1
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    #print(nums)
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
    #print(nums)
    return count
def smap(f):
    return f()

if __name__ == "__main__":
    result_alg = {"count_oper":[]}
    for i in range(20):
        pool = Pool(processes=20)
        res = [random.randrange(1, 50000, 1) for i in range(random.randrange(1, 5000, 1))]
        bubble_list_maks = copy.deepcopy(res)
        bubble_list_sofya = copy.deepcopy(res)

        # pool = Pool()
        # pool.map_async(bubble_sort_alg_maks,bubble_list_maks)
        # pool.map_async(bubble_sort_alg_sofya,bubble_list_maks)
        # pool.close()
        # pool.join()

        func1 = functools.partial(bubble_sort_alg_maks, bubble_list_maks)
        func2 = functools.partial(bubble_sort_alg_sofya, bubble_list_maks)

        pool = Pool(processes=4)
        res = pool.map(smap,[func1, func2])
        pool.close()
        pool.join()
        print(res)
  #      ret_value_1 = Array("i", bubble_list_maks)
  #      p1 = Process(target=bubble_sort_alg_maks,args=(bubble_list_maks,))
        #result_alg["count_oper"].append(count)

  #      p2 = Process(target=bubble_sort_alg_sofya,args=(bubble_list_sofya,))
        #result_alg["count_oper"].append(count)
   #     p1.start()
   #     p2.start()

 #       p1.join()
  #      p2.join()
       # print(ret_value_1.
#print(result_alg)
