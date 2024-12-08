import string

lines = iter(list(map(lambda l: l.strip(), open('input.txt').readlines())))

r = 0
for group in zip(*[lines] * 3):
    common = set(string.ascii_letters)
    
    for line in group:
        common.intersection_update(set(line))

    for c in common:
        r += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
    
print(r)