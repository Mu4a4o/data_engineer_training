##
import time
# Алгоритмы сортировки
## Пузырьковая сортировка
start = time.time()
spis = [2,4,7,8,5,6]
for i in range(len(spis) -1):
    if spis[i] > spis[i+1]:
        spis[i],spis[i+1] = spis[i+1],spis[i]
print(spis)
print(time.time()-time)