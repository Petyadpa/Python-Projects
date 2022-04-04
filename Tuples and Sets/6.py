n = int(input())

even = set()
odd = set()
for i in range(1, n + 1):
    sum_values = 0
    name = [x for x in input()]
    for el in name:
        sum_values += ord(el)
    sum_values //= i
    if sum_values % 2 == 0:
        even.add(sum_values)
    else:
        odd.add(sum_values)

sum_odd = sum(odd)
sum_even = sum(even)
result = set()
if sum_even == sum_odd:
    print(f"{', '.join(map(str, odd | even))}")
elif sum_odd > sum_even:
    print(f"{', '.join(map(str, odd.difference(even)))}")
elif sum_odd < sum_even:
    print(f"{', '.join(map(str, odd ^ even))}")
