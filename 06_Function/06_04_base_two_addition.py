b_1, b_2 = input().split()
ten_1 = int(b_1, 2)
ten_2 = int(b_2, 2)
result = bin(ten_1 + ten_2)

print(result[2:])