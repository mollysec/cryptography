from math import ceil, sqrt


n = int(input('Insert an odd number n: '))

if n % 2 == 0:
    print('The number inserted is not odd!')
else:
    x = ceil(sqrt(n))
    y2 = pow(x,2) - n

    while True:
        if y2 == pow(ceil(sqrt(y2)),2):     # check if x2 is an integral power (e.g. x2=125 is not!)
            break
        x += 1
        y2 = pow(x,2) - n

    print(f'One factor of n = {n} is m = {int(x - sqrt(y2))}')