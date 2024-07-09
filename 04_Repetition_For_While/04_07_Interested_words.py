word = input()
s = input()
word_length = len(word)

count = 0

for i in range(len(s)):
    if word == s[i:i+word_length]:
        count += 1
    if (i + word_length) == len(s):
        #print("break")
        break

print(count)
