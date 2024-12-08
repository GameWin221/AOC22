def c_to_n(c: str) -> int:
    o = ord(c)
    return o - ord('X') if c in "XYZ" else o - ord('A')

def outcome(a: int, b: int) -> int:
    return [2, 0, 1][(a + b) % 3]

    #if a == 0:
    #    if b == 0:
    #        return 2
    #    elif b == 1:
    #        return 0
    #    elif b == 2:
    #        return 1
    #elif a == 1:
    #    if b == 0:
    #        return 0
    #    elif b == 1:
    #        return 1
    #    elif b == 2:
    #        return 2
    #elif a == 2:
    #    if b == 0:
    #        return 1
    #    elif b == 1:
    #        return 2
    #    elif b == 2:
    #        return 0

guide = map(lambda l: list(map(c_to_n, l.strip().split(' '))), open('input.txt').readlines())

result = 0
for (a, b) in guide:
    result += outcome(a, b) + 1 + b * 3

print(result)