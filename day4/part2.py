lines = list(map(lambda l: l.strip(), open('input.txt').readlines()))
range_pairs = list(map(lambda l: list(map(lambda p: list(map(int, p.split('-'))), l.split(','))), lines))

r = 0
for (a, b) in range_pairs:
    a, b = set(range(a[0], a[1]+1)), set(range(b[0], b[1]+1))
    
    r += 1 if len(a.intersection(b)) > 0 or len(b.intersection(a)) > 0 else 0
    
print(r)