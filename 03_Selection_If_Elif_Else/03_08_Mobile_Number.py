n = input()
phone_format = ['06','08','09']

if len(n) == 10 and n[0:2] in phone_format:
    print("Mobile number")
else:
    print("Not a mobile number")