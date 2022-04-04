def validation(x, y):
    if x in range(0, rows) and y in range(0, len(matrix[0])):
        return True
    return False


rows = int(input())

matrix = []
for i in range(0, rows):
    matrix.append([int(x) for x in input().split()])

command = input()
while command != "END":
    action, r, c, val = command.split()
    r = int(r)
    c = int(c)
    val = int(val)
    if validation(r, c):
        if action == "Add":
            matrix[r][c] += val
        elif action == "Subtract":
            matrix[r][c] -= val
    else:
        print("Invalid coordinates")
    command = input()

for line in matrix:
    print(" ".join(map(str, line)))

