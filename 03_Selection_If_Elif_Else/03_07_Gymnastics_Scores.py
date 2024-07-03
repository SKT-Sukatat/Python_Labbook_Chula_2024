a, b, c, d = [float(x) for x in input().split()]

max = a

if b>max:
    max = b
if c>max:
    max = c
if d > max:
    max = d

result = [a, b, c, d]
result.remove(max)

min = result[0]

if min > result[1]:
    min = result[1]
if min > result[2]:
    min = result[2]

result.remove(min)

final_result = (result[0] + result[1])/2
print(final_result)
