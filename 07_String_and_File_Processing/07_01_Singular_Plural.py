word = input()

if word[-1] == 's' or word[-1] == 'x' or word[-2:] == 'ch':
    word += 'es'
elif word[-1] == 'y':
    word = word[:-1]
    word += 'ies'
else:
    word += 's'

print(word)