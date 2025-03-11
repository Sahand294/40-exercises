with open('int', 'r') as file:
    text = file.read().split()
num = 0
dup = []
output = []
pair = []
for i in text:
    if num != 2:
        pair.append(i)
        num += 1
    if num == 2:

        output.append(tuple(pair))
        pair = []
        num = 0
    dup.append(i)
print(output)
