with open('hi','r') as text:
    text = text.read().split()
dup = {}
for i in text:
    if i in  dup.keys():
        dup[i] += 1
    else:
        dup[i] = 1
unique = []
for x,i in dup.items():
    if i == 1:
        unique.append(x)
with open('hey','a') as file:
    file.writelines(unique)
    #for i in unique:
     #   file.write(i)