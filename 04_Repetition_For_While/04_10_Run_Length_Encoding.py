s = input()

char_list = []

start = 0
stop = 0

for i in range(len(s)):
    if i + 1 == len(s):
        # print(i, "break")
        run_length = s[start:]
        char_list.append(run_length)
        break
    if s[i] != s[i+1]:
        stop = i+1
        run_length = s[start:stop]
        char_list.append(run_length)
        start = stop 
    # print(i)

result = ""

for l in char_list:
    result += l[0] + " " + str(len(l)) + " "

print(result.strip())


# result = ""
# for i in range(1, len(char_list)):
#     result += char_list[i] + " "+ str(char_num[i]) + " "

# print(result.strip())