import random
import time

def generate_random_list(n):
    random_list = [random.randint(0,1000000) for _ in range(n)]
    return random_list

def Rand_quicksort(S):
    if len(S) <= 1:
        return S

    ai = random.choice(S)
    S_minus = [a for a in S if a < ai]
    S_equal = [a for a in S if a == ai]
    S_plus = [a for a in S if a > ai]  

    return Rand_quicksort(S_minus) + S_equal + Rand_quicksort(S_plus)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while arr[j] >= pivot and j >= i:
            j -= 1
        if j < i:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

if __name__ == "__main__":
    N=[100,1000,10000,100000,1000000]
    for x in N:
        arr = generate_random_list(x)

        start_time = time.time()
        sorted_arr = Rand_quicksort(arr)
        end_time = time.time()
        r_execution_time = end_time - start_time

        start_time = time.time()
        quicksort(arr,0,x-1)
        end_time = time.time()
        execution_time = end_time - start_time
        
        print('N=%d: random_quick_sort take %f sec, quick_sort take %f sec '%(x, r_execution_time, execution_time))
