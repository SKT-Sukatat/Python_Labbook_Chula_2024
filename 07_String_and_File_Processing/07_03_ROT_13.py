letter = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i' \
          , 'j', 'k', 'l', 'm','n','o','p','q','r' \
            ,'s','t','u', 'v', 'w','x','y','z']

result = []

while True:
    sentence = input()
    new_sentence = ""

    if sentence != 'end':
        for i in sentence:
            if i.lower() in letter and i.islower():
                index = letter.index(i.lower())
                i = letter[(index + 13)%26]
                new_sentence += i
            elif i.lower() in letter and i.isupper():
                index = letter.index(i.lower())
                i = letter[(index + 13)%26].upper()
                new_sentence += i
            else:
                new_sentence += i
        result.append(new_sentence)
    else:
        break
print("___________________________")
for sentence in result:
    print(sentence)
