import random
import time

testarr = []
for i in range(1000):
    testarr.append(1000 - i)

print(testarr)


def sort(arr):
    if len(arr) > 1:
        opel = arr[len(arr) // 2]
        larr = []
        rarr = []
        for i in range(len(arr)):
            if arr[i] < opel:
                larr.append(arr[i])
            elif arr[i] > opel:
                rarr.append(arr[i])
        larr = sort(larr)
        rarr = sort(rarr)
        arr = larr + [opel] + rarr
    return arr


start_time = time.time()
print(sort(testarr))
end_time = time.time()
print(end_time - start_time)

testarr = random.sample(range(1000), 1000)
print(testarr)

start_time = time.time()
print(sort(testarr))
end_time = time.time()
print(end_time - start_time)
