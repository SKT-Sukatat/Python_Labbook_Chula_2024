n = [int(x) for x in input().split()]
unique_list = []

for x in n:
    if x not in unique_list:
        unique_list.append(x)

unique_list.sort()
n = unique_list

count = 0

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        count += 1

if n[-1] != n[-2]:
    count += 1

print(count)
print(n[:10])