import math

a, b, c = input().split(',')

nb = len(b)
nc = len(c)

n = int(a+b+c) - int(a+b)
d = 10**(nb+nc) - 10**nb

gcd = math.gcd(n, d)
n /= gcd
d /= gcd

print(str(int(n))+ ' / ' + str(int(d)))