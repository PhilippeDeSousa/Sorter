import time
import numpy as np

def swap(nbs, n1, n2):
    tmp = nbs[n1]
    nbs[n1] = nbs[n2]
    nbs[n2] = tmp

def recurSort(numbers, count):
    if (len(numbers) > 1):
        len_nb = len(numbers)
        fp = numbers[:len_nb // 2]
        sp = numbers[len_nb // 2:]
        len_fp = len(fp)
        len_sp = len(sp)

        count = recurSort(fp, count) + recurSort(sp, count)

        i = 0; j = 0; k = 0

        while i < len_fp and j < len_sp:
            if fp[i] < sp[j]:
                numbers[k] = fp[i]
                i+=1
            else:
                numbers[k] = sp[j]
                j+=1
            k+=1
            count+=1
        
        for pos in range(i, len_fp):
            numbers[k] = fp[pos]
            k+=1
        
        for pos in range(j, len_sp):
            numbers[k] = sp[pos]
            k+=1
        return count
    else:
        return 0

def sort(numbers):
    count = 0
    t0 = time.time()

    count = recurSort(numbers, 0)

    t1 = time.time()
    print('----------------------------------------------------------')
    print('Merge sort:', count, 'comparisons for', len(numbers), 'numbers')
    print('Time elapsed:', t1 - t0)
    print('----------------------------------------------------------')