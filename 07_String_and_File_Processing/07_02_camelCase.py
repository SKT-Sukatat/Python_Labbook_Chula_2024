## Bad Method Too Long, and Complex
## Please Check Ajarn Somchai's Video 

sentence = input().split()

for i in range(len(sentence)):
    if sentence[i][0] == '"' and sentence[i][-1] == '"':
        sentence[i] = sentence[i][1:-1]
        sentence.insert(i, sentence[i])
        del sentence[i]
    elif sentence[i].find('-') > 0:
        sentence[i] = sentence[i].split('-')
        print(sentence[i][2])
        for j in range(len(sentence[i])):
            # print(j)
            sentence.insert(i+j, sentence[i+j][j])
    

for i in range(len(sentence)):
    if type(sentence[i]) == list:
        del sentence[i]


for i in range(len(sentence)):
    if i == 0:
        sentence[i] = sentence[i].lower()
    elif sentence[i] == '-':
        del sentence[i]
    else:
        sentence[i] = sentence[i][0].upper() + sentence[i][1:].lower()
camelCase = "".join(sentence)

print(camelCase)