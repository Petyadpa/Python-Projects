line = [x for x in input()]
line = tuple(line)

occurrences = {}
for el in line:
    if el not in occurrences:
        occurrences[el] = 0
    occurrences[el] += 1
occurrences = sorted(occurrences.items(), key=lambda kv: kv[0])

[print(f"{k}: {v} time/s") for k, v in occurrences]
