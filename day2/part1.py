def c_to_n(c: str) -> int:
    o = ord(c)
    return o - ord('X') if c in "XYZ" else o - ord('A')

def outcome(a: int, b: int) -> int:
    return [3, 0, 6][b - a] # [3, 0, 6][(b-1) - (a-1)]

    #if a == 1:
    #    if b == 1:
    #        return 3
    #    elif b == 2:
    #        return 0
    #    elif b == 3:
    #        return 6
    #elif a == 2:
    #    if b == 1:
    #        return 6
    #    elif b == 2:
    #        return 3
    #    elif b == 3:
    #        return 0
    #elif a == 3:
    #    if b == 1:
    #        return 0
    #    elif b == 2:
    #        return 6
    #    elif b == 3:
    #        return 3

guide = map(lambda l: list(map(c_to_n, l.strip().split(' '))), open('input.txt').readlines())

result = 0
for (a, b) in guide:
    result += outcome(b, a) + b + 1

print(result)