all_grades = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
grades = []
ids = []
uids = []

while True:
    data = input()
    if data == 'q':
        choosen_uid = [x for x in input().split()]
        for i in range(len(choosen_uid)):
            uids.append(choosen_uid[i])
        break
    else:    
        id, grade = data.split()
        ids.append(id)
        grades.append(grade)

for uid in uids:
    if uid in ids:
        index = ids.index(uid)
        grade = grades[index]
        new_grade = all_grades[all_grades.index(grade) + 1]
        grades[index] = new_grade


for i in range(len(ids)):
    print(ids[i], grades[i])