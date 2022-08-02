#Simple implementation of binary search algorithm
# - ONLY WORKS IF ARRAY/LIST IS SORTED!!!!

#We will prove that binary search is faster than naive search
# - naive search: scan entire list and ask if its equal to the target
#   if yes, return index | if no, then return -1

import random
import time

def naive_search(l, target):
    #example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

#binary search makes use of divide and conquer
def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0 #lowest index
        high = len(l) - 1 #highest index

    if high < low: #if target is not in the list, return -1
        return -1

    #example l = [1, 3, 5, 10, 12]
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target, low, midpoint - 1) #move highest down
    elif target > l[midpoint]:
        return binary_search(l,target, midpoint + 1, high) #move lowest up

if __name__ =='__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10

    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive Search Time Average: ", (end - start)/ length, " seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary Search Time Average: ", (end - start)/ length, " seconds")