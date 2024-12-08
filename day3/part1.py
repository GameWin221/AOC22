lines = list(map(lambda l: l.strip(), open('input.txt').readlines()))

r = 0
for line in lines:
    a, b = set(line[:len(line)//2]), set(line[len(line)//2:])

    for c in a.intersection(b):
        r += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
    
print(r)