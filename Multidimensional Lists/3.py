import sys

row, col = [int(x) for x in input().split()]

m = []
for _ in range(row):
    m.append([int(x) for x in input().split()])

sum_max = -sys.maxsize
starting_point = None

for i in range(0, row - 2):
    for j in range(1, col - 1):
        sum_matrix = m[i][j - 1] + m[i][j] + m[i][j + 1] \
                     + m[i + 1][j - 1] + m[i + 1][j] + m[i + 1][j + 1] \
                     + m[i + 2][j - 1] + m[i + 2][j] + m[i + 2][j + 1]
        if sum_matrix > sum_max:
            sum_max = sum_matrix
            starting_point = (i, j)
print(f"Sum = {sum_max}")

i, j = starting_point
print(' '.join(map(str, [m[i][j - 1], m[i][j], m[i][j + 1]])))
print(' '.join(map(str, [m[i + 1][j - 1], m[i + 1][j], m[i + 1][j + 1]])))
print(' '.join(map(str, [m[i + 2][j - 1], m[i + 2][j], m[i + 2][j + 1]])))
