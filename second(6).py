import random
import time

testarr = [random.randint(-100000000000, 0), random.randint(0, 100000000000)]
print(testarr)


def f(x):
    return -(x**3)+200

def binsearch1(f, arr):
    krit = f(arr[0]) * f(arr[1])
    if krit < 0:
        if f((arr[0] + arr[1]) / 2) == 0:
            print(arr, f(arr[0]))
            file = open("log1.txt", "w")
            file.write(f"{(arr[0] + arr[1]) / 2}")
            file.close()
        elif f(arr[0]) * f((arr[0] + arr[1]) / 2) < 0:
            arr = [arr[0], (arr[0] + arr[1]) / 2]
        elif f(arr[1]) * f((arr[0] + arr[1]) / 2) < 0:
            arr = [(arr[0] + arr[1]) / 2, arr[1]]
        if abs(arr[0] - arr[1]) < 0.00001:
            print(arr, f(arr[0]))
            file = open("log1.txt", "w")
            file.write(f"{(arr[0] + arr[1]) / 2}")
            file.close()
        else:
            binsearch1(f, arr)
    elif krit > 0:
        print("нет корней")
        file = open("log1.txt", "w")
        file.write(f"нет корней")
        file.close()
    elif krit == 0:
        if f(arr[0]) == 0:
            arr[1] = arr[0]
            print(arr, f(arr[0]))
            file = open("log1.txt", "w")
            file.write(f"{(arr[0] + arr[1]) / 2}")
            file.close()
        elif f(arr[1]) == 0:
            arr[0] = arr[1]
            print(arr, f(arr[0]))
            file = open("log1.txt", "w")
            file.write(f"{(arr[0] + arr[1]) / 2}")
            file.close()





def binsearch2(f, arr):
    krit = 0
    while abs(arr[0] - arr[1]) > 0.00001:
        krit = f(arr[0]) * f(arr[1])
        if krit < 0:
            if f((arr[0] + arr[1]) / 2) == 0:
                print(arr, f(arr[0]))
                break
            elif f(arr[0]) * f((arr[0] + arr[1]) / 2) < 0:
                arr = [arr[0], (arr[0] + arr[1]) / 2]
            elif f(arr[1]) * f((arr[0] + arr[1]) / 2) < 0:
                arr = [(arr[0] + arr[1]) / 2, arr[1]]
        elif krit > 0:
            print("нет корней")
            file = open("log2.txt", "w")
            file.write(f"нет корней")
            file.close()
            break
        elif krit == 0:
            if f(arr[0]) == 0:
                break
            elif f(arr[1]) == 0:
                break
    if krit <= 0:
        print(arr, f(arr[0]))
        file = open("log2.txt", "w")
        file.write(f"{(arr[0] + arr[1]) / 2}")
        file.close()

start_time1 = time.time()
binsearch1(f, testarr)
end_time1 = time.time()
file = open("log1.txt", "a")
file.write(f" time = {end_time1-start_time1}")
file.close()



start_time2 = time.time()
binsearch2(f, testarr)
end_time2 = time.time()
file = open("log2.txt", "a")
file.write(f" time = {end_time2-start_time2}")
file.close()