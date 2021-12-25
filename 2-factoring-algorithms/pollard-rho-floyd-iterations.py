import random
from gmpy2 import gcd
from math import ceil


print('Insert an odd number n:')
n = int(input())
print('Insert a bound T:')
t = int(input())

if n % 2 == 0:
    print('The number inserted is not odd!')
else:
    zn = [x for x in range(n)]
    # print('Zn :', zn)
    a = random.choice(zn)
    print(f'The random choice is a = {a}')
    
    y1 = (pow(a,2)+1) % n                        # compute first and second iterates
    y2 = (pow(y1,2)+1) % n
    m = 1
    check = True
    while m <= t:
        d = gcd(ceil(y1-y2), n)           # convert y1-y2 from float to integer in order to apply igcd
        if d > 1 and d < n:
            print(f'One factor of n = {n} is d = {d}')
            check = False
            break
        else:
            m += 1
            y1 = y2
            y2 = (pow(y1,2)+1) % n
            print(y1, y2)
    
    if check:
        print(f'No non-trivial factors of n = {n} have been found after T = {t} iterations.')
        print('Restart the algorithm with a larger T or a new random choice.')
