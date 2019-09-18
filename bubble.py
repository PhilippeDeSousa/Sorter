import time

def swap(nbs, n1, n2):
    tmp = nbs[n1]
    nbs[n1] = nbs[n2]
    nbs[n2] = tmp

def sort(numbers):
    count = 0
    t0 = time.time()
    for pos in range(len(numbers) -1, 0, -1):
        for i in range(pos):
            if (numbers[i] > numbers[i + 1]):
                swap(numbers, i, i+1)
                count += 1

    t1 = time.time()
    print('----------------------------------------------------------')
    print('Bubble sort:', count, 'comparisons for', len(numbers), 'numbers')
    print('Time elapsed:', t1 - t0)
    print('----------------------------------------------------------')