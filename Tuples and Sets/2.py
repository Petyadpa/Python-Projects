n,m = input().split()

set_one = set()
set_two = set()

for i in range(int(n)+int(m)):
    nums = int(input())
    if i in range(int(n)):
        set_one.add(nums)
    else:
        set_two.add(nums)
result = set_one & set_two
for el in result:
    print(el)
