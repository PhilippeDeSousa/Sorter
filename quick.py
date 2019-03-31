import time

def swap(nbs, n1, n2):
    tmp = nbs[n1]
    nbs[n1] = nbs[n2]
    nbs[n2] = tmp

def recurSort(numbers, count):
    if (len(numbers) > 1):
        pivot_idx = 0
        pivot = numbers[0]
        
        for i in range(len(numbers) - 1):
            if numbers[i+1] < pivot:
                swap(numbers, i+1, pivot_idx+1)
                pivot_idx += 1
            count+=1
        swap(numbers, 0, pivot_idx)
        fp, count = recurSort(numbers[:pivot_idx], count)
        sp, count = recurSort(numbers[pivot_idx + 1:], count)
        fp.append(numbers[pivot_idx])

        return fp + sp, count

    return numbers, count

def sort(numbers):
    count = 0
    t0 = time.time()

    numbers, count = recurSort(numbers, 0)

    t1 = time.time()
    print('----------------------------------------------------------')
    print('Quicksort sort:', count, 'comparisons for', len(numbers), 'numbers')
    print('Time elapsed:', t1 - t0)
    print('----------------------------------------------------------')