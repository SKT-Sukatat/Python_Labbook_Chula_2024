h = int(input())

print((h-1)*" " + "*")
for i in range(2, h):
    print((h-i) * " " + "*" +  (2*(i-1) -1) * " " + "*")

print((2*h - 1)*"*")