n = int(input())


result = set()

for i in range(n):
    intrsc1, intrsc2 = input().split("-")

    first_start = int(intrsc1.split(",")[0])
    first_end = int(intrsc1.split(",")[1])
    second_start = int(intrsc2.split(",")[0])
    second_end = int(intrsc2.split(",")[1])

    int1 = set()
    int2 = set()


    for el in range(first_start, first_end + 1):
        int1.add(el)
    for el in range(second_start, second_end + 1):
        int2.add(el)
    new = int1 & int2
    if len(new) > len(result):
        result = new

result = list(result)

print(f"Longest intersection is {result} with length {len(result)}")
