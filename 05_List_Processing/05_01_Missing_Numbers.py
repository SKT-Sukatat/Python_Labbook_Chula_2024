n = list(input())
zero_to_nine = ['0','1','2','3','4','5','6','7','8','9']
missing_numbers = []

for i in range(len(zero_to_nine)):
    if zero_to_nine[i] not in n:
        missing_numbers.append(zero_to_nine[i])

if len(missing_numbers) != 0:
    result = [int(i) for i in missing_numbers]
    result = str(result)[1:-1]
else:
    result = "None"
    
print(result)