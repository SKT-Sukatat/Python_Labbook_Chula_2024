n = input()
l = []

while n != 'q':
    l += [float(n)]
    n = input()
    if n == 'q':
        break

total = 0
for i in range(len(l)):
    total += l[i]

if len(l) != 0:
    mean = total/len(l)
    print(round(mean,2))
else:
    print("No Data")