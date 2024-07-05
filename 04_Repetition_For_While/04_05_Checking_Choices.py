solution = input()
answer = input()

result = 0

if len(answer) != len(solution):
    result = "Incomplete answer"
else:
    for i in range(len(solution)):
        # print((answer[i] == solution[i]), "and", (answer[i] != " "))
        # print((answer[i] == solution[i]) and (answer[i] != " "))
        # print("Solution:", solution[i],  "Answer: ", answer[i])
        # print("__________")
        if (answer[i] == solution[i]) and (answer[i] != " "):
            result += 1
            #print("pb", i, "solution:", solution[i], "answer:", answer[i], "results:", result)

print(result)