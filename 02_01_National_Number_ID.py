n = [x for x in input()]

inner_term = 13*float(n[0]) + 12*float(n[1]) +11*float(n[2]) + 10*float(n[3]) + 9*float(n[4]) \
    + 8*float(n[5]) + 7*float(n[6]) + 6*float(n[7]) + 5*float(n[8]) + 4*float(n[9]) + 3*float(n[10]) + 2*float(n[11])
n12 = (11 - (inner_term%11))%10

x1 = n[0]
x2 = n[1]+n[2]+n[3]+n[4]
x3 = n[5]+n[6]+n[7]+n[8]+n[9]
x4 = n[10]+n[11]
x5 = str(int(n12))

print(x1, x2, x3, x4, x5)