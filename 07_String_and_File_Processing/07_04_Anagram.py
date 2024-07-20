original = input().lower()
anagram = input().lower()

original_length = 0
for word in original.split():
    original_length += len(word)

valid_char = 0

for char in original:
    for ana_char in anagram:
        if char == ana_char and ana_char != " ":
            valid_char += 1
            break

if valid_char == original_length:
    print("YES")
else:
    print("NO")
