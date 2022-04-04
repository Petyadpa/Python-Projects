rows, cols = [int(x) for x in input().split()]

matrix = []
for i in range(0, rows):
    matrix.append([x for x in input().split()])

command = input()

while not command == "END":

    data = command.split()

    if len(data) == 5 and data[0] == "swap":
        c1 = int(data[1])
        c2 = int(data[2])
        c3 = int(data[3])
        c4 = int(data[4])
        if c1 not in range(0, rows) or c2 not in range(0, cols) or c3 not in range(0, rows) or c4 not in range(0, cols):
            print("Invalid input!")
            command = input()
            continue
        else:
            old = matrix[c1][c2]
            matrix[c1][c2] = matrix[c3][c4]
            matrix[c3][c4] = old
            for i in range(rows):
                for j in range(cols):
                    print(matrix[i][j], end=" ")
                print()
    else:
        print("Invalid input!")
        command = input()
        continue
    command = input()
