file_name, year = input().split()
sids = []
scores = []

selected_scores = []


with open(file_name) as my_file:
    for line in my_file.readlines():
        sid, score = line[:-2].split(" ")
        sids.append(sid)
        scores.append(score)

    for sid in sids:
        if sid[:2] == year[2:]:
            selected_index = sids.index(sid)
            selected_scores.append(float(scores[selected_index]))

if len(selected_scores) != 0:
    averge_score = round(sum(selected_scores)/len(selected_scores),1)
    print(float(min(selected_scores)), float(max(selected_scores)), averge_score)
else:
    print("No data")