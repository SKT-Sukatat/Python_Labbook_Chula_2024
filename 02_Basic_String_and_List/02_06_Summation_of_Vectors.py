# take u and v as input
u = input()
v = input()

u_list = list(u[1:-1].split(", "))
v_list = list(v[1:-1].split(", "))

# cast all input to float type
u1, u2, u3 = float(u_list[0]), float(u_list[1]), float(u_list[2])
v1, v2, v3 = float(v_list[0]), float(v_list[1]), float(v_list[2])

x1 = u1 + v1
x2 = u2 + v2
x3 = u3 + v3

# Summation of Vectors
print(type(u_list[0]))
print( '[' + str(u1) + ', '+ str(u2) + ', ' + str(u3) + '] + ' + \
      '[' + str(v1) + ', '+ str(v2) + ', ' + str(v3) + '] = [' +  \
       str(x1) +', ' + str(x2) + ', ' + str(x3) + ']')