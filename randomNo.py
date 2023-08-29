def random(n):
    n = n * 1566083941
    if n<0:
        n = n + +2147483647+1
        n = n* 1566083941
        if n < 0:
           random = n * 4.6566128752458*10**(-10)
    return random

print(random(3))