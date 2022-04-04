from collections import deque

name = input()
queue = deque()
while not name == "End":
    if not name == "Paid":
        queue.append(name)
    if name == "Paid":
        while queue:
            print(queue.popleft())
    name = input()

print(f"{len(queue)} people remaining.")
