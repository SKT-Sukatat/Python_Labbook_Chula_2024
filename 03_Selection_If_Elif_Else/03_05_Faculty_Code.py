codes = [str(x) for x in range(20,41)]
codes += ['01', '02', '51', '53','55','58']

code = input()

if code in codes:
    print("OK")
else:
    print("Error")