import math

# a = int(input())
# b = int(input())
# c = int(input())
a, b, c = [float(x) for x in input().split()]

root_term = math.sqrt(b**2 - 4*a*c)

x1 = (- b - root_term)/(2*a)
x2 = (- b + root_term)/(2*a)

print(round(x1, 3), round(x2,3))