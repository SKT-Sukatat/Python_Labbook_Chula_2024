n = int(input())

if n < 1000:
    r = n
elif n < 10**4:
    r = str(round(n / 10**3 ,1)) + "K"
elif n < 10**7:
    r = str(round(n / 10**3,0))[:-2] + "K"
elif n < 10**8: #2.3M
    r = str(round(n / 10**6 ,1)) + "M"
elif n < 10**10:
    r = str(round(n / 10**6,0))[:-2] + "M"
elif n < 10**12:
    r = str(round(n / 10**9 ,1)) + "B"
else:
    r = str(round(n / 10**9,0))[:-2] + "B"