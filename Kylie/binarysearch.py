import time, random

def naive_search(list, target):
    for i in list:
        if i == target:
            return i 
    return -1

def binary_search(list, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    mid = (low+high) // 2

    if list[mid] == target:
        return target
    
    elif list[mid] < target:
        return binary_search(list, target, low, mid-1)
    elif list[mid] > target:
        return binary_search(list, target,mid+1, high)
    
   

if __name__ == '__main__':
    length = 100000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()

    print(f"Naive search took {end-start} time to search")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()

    print(f"Binary search took {end-start} time to search")