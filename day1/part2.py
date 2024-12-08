import itertools as it

lines = map(lambda x: x.strip(), open('input.txt').readlines())
top = [0, 0, 0]
s = 0
for line in lines:
    if line != '':
        s += int(line)
    else:
        if s > top[0]:
            top = [s] + top[0:2]
        elif s > top[1]:
            top = [top[0]] + [s] + [top[1]]
        elif s > top[2]:
            top = top[0:2] + [s]
            
        s = 0
        
if s > top[0]:
    top = [s] + top[0] + top[1]
elif s > top[1]:
    top = top[0] + [s] + top[1]
elif s > top[2]:
    top = top[0] + top[1] + [s]
    
print(sum(top))