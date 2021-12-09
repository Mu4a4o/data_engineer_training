import numpy as np
import random
import datetime
from multiprocessing import Pool

def sum_num (val):
    k = 0
    for l in range(100):
        for i in val:
            k = k + i
    return k



num_list = np.array([random.randrange(0,10) for i in range(0,9999999)])
print('end_gener_one')

a = datetime.datetime.now()
print(sum_num(num_list))
print(datetime.datetime.now() - a)
print('end_one_proc')

a = datetime.datetime.now()
p = Pool(processes = 16)
print(sum(p.map(sum_num,np.array_split(num_list,16))))
print(datetime.datetime.now() - a)
print('end_multy_proc')




