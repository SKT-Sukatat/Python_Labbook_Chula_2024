n = int(input())
name = {}

for i in range(n):
    key, value = input().split()
    name[key] = value

m = int(input())
words = []

for i in range(m):
    word = input()
    words.append(word)

for w in words:
    if w in name.keys():
        print(name[w])
    elif w in name.values():
        for k, v in name.items():
            if v == w:
                print(k)
    else:
        print("Not found")