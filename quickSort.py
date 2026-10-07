def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in arr[1:]:
            if i < pivot:
                less.append(i)
            else:
                greater.append(i)
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quicker_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr)//2]
        less = []
        greater = []
        for i in arr[1:]:
            if i < pivot:
                less.append(i)
            else:
                greater.append(i)
        return quick_sort(less) + [pivot] + quick_sort(greater)

import random
import time
# example = []
start_time = time.time()
print("Creating List")
# for i in range(999999999999):
#     example.append(random.randint(0,99999999))
example = random.sample(range(10000000000), 100000000)

print("List Created")
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
# print(quick_sort(example))
quick_sort(example)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
quicker_sort(example)
# print(quicker_sort(example))
print("--- %s seconds ---" % (time.time() - start_time))