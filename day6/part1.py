result = -1

data = open('input.txt').read().strip()
for i in range(len(data)-4):
    if len(set(data[i:i+4])) == 4:
        result = i+4
        break
    
print(result)