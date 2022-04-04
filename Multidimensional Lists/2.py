rows, cols = [int(x) for x in input().split()]

matrix = []
count = 0

for i in range(0,rows):
    matrix.append([x for x in input().split()])

for i in range(rows-1,0,-1):
    for j in range(cols-1,0,-1):
        if matrix[i][j] == matrix[i-1][j-1] == matrix[i-1][j] == matrix[i][j-1]:
            count += 1
print(count)
