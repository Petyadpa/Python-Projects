text = list(input())

result = ""
for el in range(len(text)):
    result += text.pop()
print(result)
