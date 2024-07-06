d = int(input())
m = int(input())
y = int(input())
y -= 543

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m <= 2:
    print(sum(days_in_month[:m-1])+ d)
# elif y % 4 != 0 and m >= 1:
#     print(sum(days_in_month[:0])+ d)
elif y % 4 == 0 and m > 2:
    print(sum(days_in_month[:m-1]) + d + 1)
else:
    print(sum(days_in_month[:m-1]) + d)