result = -1

data = open('input.txt').read().strip()
for i in range(len(data)-14):
    if len(set(data[i:i+14])) == 14:
        result = i+14
        break
    
print(result)