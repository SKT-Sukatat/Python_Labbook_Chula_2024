# Step 0: Take input
n = input()

# Step 1
step_1 = (n[3] + n[10] + n[17] + n[24] + n[31])

# Step 2
step_2 = (n[7] + n[12] + n[17] + n[22] + n[27])

# Step 3
step_3 = int(step_1) + int(step_2) + 10000

# Step 4 & 5
step_4 = str(step_3 % 10000)[0] + str(step_3 % 1000)[0] + str(step_3 % 100)[0]
sum_of_step_4 = int(str((int(step_4[0]) + int(step_4[1])+ int(step_4[2])) % 10)[0]) + 1
print(sum_of_step_4)

# Step 6
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J']
selected_letter = letter[sum_of_step_4 - 1]

# Step 7
step_7 = step_4 + selected_letter
print(step_7)
