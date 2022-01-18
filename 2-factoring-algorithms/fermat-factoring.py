#################################################
#### Use it when 'p' and 'q' are quite close ####
#################################################

from math import ceil
from gmpy2 import iroot, divexact


n = int(input('Insert an odd number n: '))

x = ceil(iroot(n,2)[0])
y2 = n - pow(x,2)

while True:
    if y2 == pow(ceil(iroot(y2,2)[0]),2):     # check if x2 is an integral power (e.g. x2=125 is not!)
        break
    x += 1
    y2 = pow(x,2) - n

p = x - iroot(y2,2)[0]
print('p =', p)

q = int(divexact(n,p))
print('q =', q)

