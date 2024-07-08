names = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward' ,'Sarah', 'Andrew', 'Anthony', 'Deborah']
nicknames = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

n = int(input())
list_input = []

for i in range(n):
    new_names = input()
    list_input.append(new_names)

for i in range(len(list_input)):
    r = 0
    for j in range(len(names)):
        if list_input[i] == names[j]:
            print(nicknames[j])
            break
        elif list_input[i] == nicknames[j]:
            print(names[j])
            break
        r += 1
        
    if r == 10:
        print("Not Found") 