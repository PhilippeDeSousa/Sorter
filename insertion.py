import time
from collections import deque

def swap(nbs, n1, n2):
    tmp = nbs[n1]
    nbs[n1] = nbs[n2]
    nbs[n2] = tmp

def sort(nbs):
    count = 0

    numbers = deque()
    n = deque(nbs)

    t0 = time.time()

    numbers.append(n[0])
    n.popleft()

    for _ in range(1, len(n)):
        pos = 0

        if len(n) > 0 and n[0] <= numbers[0]:
            numbers.appendleft(n[0])
            n.popleft()
            count += 1
        while len(n) > 0 and n[0] > numbers[pos]:
            pos += 1
            if pos == len(numbers):
                numbers.append(n[0])
                n.popleft()
                pos = 0
            count += 1
        if len(n) > 0:
            count += 1
            numbers.insert(pos, n[0])
            n.popleft()

    t1 = time.time()
    print('----------------------------------------------------------')
    print('Insertion sort:', count, 'swaps for', len(numbers), 'numbers')
    print('Time elapsed:', t1 - t0)
    print(list(numbers))
    print('----------------------------------------------------------')