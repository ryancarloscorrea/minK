import random

def randomizedPartition(arr, start, stop):
    pivotRandom = random.randrange(start, stop)
    arr[start], arr[pivotRandom] = arr[pivotRandom], arr[start]
    pivot = start
    i = start + 1
    # j começa com (start + 1) pois o pivo é o primeiro elemento [0]
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = \
        arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot
