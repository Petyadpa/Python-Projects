def checkSum(x,y):
    def trap(i,j):
        if matrix[i][j] == "X":
            return True
        return False

    for el in range(y+1, n):
        if trap(x,el):
            break
        values["right"] += int(matrix[x][el])
        path["right"].append([x, el])

    for el in range(0, y):
        if trap(x, el):
            break
        values["left"] += int(matrix[x][el])
        path["left"].append([x, el])

    for el in range(x-1, -1,-1):
        if trap(el, y):
            break
        values["up"] += int(matrix[el][y])
        path["up"].append([el, y])

    for el in range(x+1, n):
        if trap(el, y):
            break
        values["down"] += int(matrix[el][y])
        path["down"].append([el, y])


n = int(input())

matrix = []
values = {"up":0,"down":0, "left":0, "right":0}
path = {"up":[],"down":[], "left":[], "right":[]}
direction = ""
max_val = ""
is_found = False

for i in range(0,n):
    matrix.append([x for x in input().split()])

for row in range(0, n):
    for col in range(0, n):
        if matrix[row][col] == "B":
            checkSum(row, col)
            max_val = max(values.values())
            for key, value in values.items():
                if max_val == value:
                    direction = key
                    is_found = True
                    break
        if is_found:
            break
    if is_found:
        break

print(direction)
for key, val in path.items():
    if direction == key:
        print("\n".join(map(str, val)))
print(max_val)
