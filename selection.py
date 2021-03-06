import time

def swap(nbs, n1, n2):
    tmp = nbs[n1]
    nbs[n1] = nbs[n2]
    nbs[n2] = tmp

def sort(numbers):
    count = 0
    t0 = time.time()
    for i in range(len(numbers)):
        min_idx = i
        for l in range(i + 1, len(numbers)):
            if numbers[l] < numbers[min_idx]:
                min_idx = l
                count += 1
        swap(numbers, i, min_idx)
    

    t1 = time.time()
    print('----------------------------------------------------------')
    print('Selection sort:', count, 'comparisons for', len(numbers), 'numbers')
    print('Time elapsed:', t1 - t0)
    print('----------------------------------------------------------')