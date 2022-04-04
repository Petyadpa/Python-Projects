n = int(input())

matrix = []
primary = secondary = 0
for i in range(0, n):
    matrix.append([int(x) for x in input().split()])

for row in range(0, n):
    for col in range(0, n):
        if row == col:
            primary += matrix[row][col]
        if row + col == n - 1:
            secondary += matrix[row][col]
print(abs(primary - secondary))
