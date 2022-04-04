def create_blank_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        matrix.append([])
        for _ in range(cols):
            matrix[-1].append(0)

    return matrix


rows, cols = [int(x) for x in input().split()]
count = 0

string = [x for x in input()]
for el in range((rows * cols) - len(string)):
    string += string[el]

matrix = create_blank_matrix(rows, cols)

for i in range(0, rows):
    for j in range(cols):
        matrix[i][j] = string[count]
        count += 1

for el in range(rows):
    result = ""
    if el == 0:
        for j in range(cols):
            result += matrix[el][j]
        print(''.join(result), sep="\n")
    elif el % 2 == 0 :
        for j in range(cols):
            result += matrix[el][j]
        print(''.join(result), sep="\n")
    else:
        for j in range(cols - 1, -1, -1):
            result += matrix[el][j]
        print(''.join(result),)
