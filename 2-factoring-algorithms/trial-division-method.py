from gmpy2 import c_mod


n = int(input('Insert the number n: '))
t = int(input('Insert the bound T: '))

check = True
for m in range(2, t+1):
    if int(c_mod(n,m)) == 0:
        print(f'One factor of n = {n} is m = {m}')
        check = False
        break

if check:
    print(f'The number n = {n} has not divisors up to T = {t}')
