n = int(input())

data = []

for i in range(n):
    n1, n2 = [int(x) for x in input().split()]
    data.append(n1)
    data.append(n2)

list_1 = []
list_2 = []

# Red Line #1
for i in range(0, len(data), 4):
    list_1.append(data[i])
    if (i + 4) > len(data):
        break

# Red Line #2
for i in range(3, len(data), 4):
    list_1.append(data[i])
    if (i + 4) > len(data):
        break

# Blue Line #1
for i in range(1, len(data), 4):
    list_2.append(data[i])
    if (i + 4) > len(data):
        break

# Blue Line #1
for i in range(2, len(data), 4):
    list_2.append(data[i])
    if (i + 4) > len(data):
        break

mode = input()

if mode == 'Zig-Zag':
    print(min(list_1), max(list_2))
elif mode == 'Zag-Zig':
    print(min(list_2), max(list_1))