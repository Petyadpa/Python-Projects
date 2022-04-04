import re

initial_data = input()
data =[x.split() for x in re.split("[|]", initial_data)][::-1]
print(" ".join(map(str, [item for sublist in data for item in sublist])))
