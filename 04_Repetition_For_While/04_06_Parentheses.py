a = list(input())

original_a = a

for i in range(len(a)):
    if a[i] == '(':
        a[i] = '['
    elif a[i] == '[':
        a[i] = '('
    elif a[i] == ')':
        a[i] = ']'
    elif a[i] == ']':
        a[i] = ')'

a = "".join(a)

if a != original_a:
    print(a)
else:
    print(a)
    print("no parentheses") 