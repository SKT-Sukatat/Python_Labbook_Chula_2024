a = float(input())
a_copy = a

l = 0

u = 0

while a_copy // 10 != 0:
    u += 1
    a_copy = a_copy // 10

print("Pass")

x = (l+u)/2

while abs(a-(10**x)) >= (10**(-10))*max(a,10**x):
    print(round(x, 6))
    x = (l+u)/2
    if 10**x > a:
        u = x
    elif 10**x < a:
        l =x

print(round(x, 6))