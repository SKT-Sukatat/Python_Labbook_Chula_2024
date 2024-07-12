result = []
n = int(input())
show_result = str(int(n))

while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    result.append(n)

if len(result) < 15:
    for i in range(len(result)):
        show_result += "->" + str(int(result[i]))
else:
    show_result = str(int(result[-15]))
    for i in range(-14, 0):
        show_result += "->" + str(int(result[i]))

print(show_result)