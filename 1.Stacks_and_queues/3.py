line = input()
stack = []

for i in range(len(line)):
    if line[i] == "(":
        stack.append(i)
    elif line[i] == ")":
        start_index = stack.pop()
        print(line[start_index:i+1])
