a = float(input())

l = 0; u = a
x = (l+u)/2

while abs(a-10**x) >= (10**(-10))*max(a,10**x):
    x = (l+u)/2
    if 10**x > a:
        u = x
    elif 10**x < a:
        l =x

print(round(x, 6))