result = []

# Set 1
set_1 = int(input())

for i in range(set_1):
    x = int(input())
    if len(result) % 2 == 0:
        result.append(x)
    elif len(result) % 2 == 1:
        result.insert(0, x)

# Set 2
set_2 = [int(a) for a in input().split()]

for j in range(len(set_2)):
    if len(result) % 2 == 0:
        result.append(set_2[j])
    elif len(result) % 2 == 1:
        result.insert(0, set_2[j])

# Set 3
while True:
    z = int(input())
    if z == -1:
        break
    elif len(result) % 2 == 0:
        result.append(z)
    elif len(result) % 2 == 1:
        result.insert(0, z)

print(result)