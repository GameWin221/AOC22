import itertools as it

lines = map(lambda x: x.strip(), open('input.txt').readlines())
ms = 0
s = 0
for line in lines:
    if line != '':
        s += int(line)
    else:
        if s > ms:
            ms = s
        s = 0
        
if s > ms:
    ms = s
    
print(ms)