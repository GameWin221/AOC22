lines = list(map(lambda l: l.removesuffix('\n'), open('input.txt').readlines()))
split_line = lines.index('')

stack_lines = lines[:split_line-1]
stack_numbers_line = lines[split_line-1]
instruction_lines = lines[split_line+1:]

stack_count = max(map(int, stack_numbers_line.split('   ')))
stacks = [[] for _ in range(stack_count)] # weird error when doing [[]]* stack_count

for line in stack_lines:
    for (stack_id, i) in enumerate(range(1, len(line), 4)):
        c = line[i]
        if c != ' ':
            stacks[stack_id].append(c)

for line in instruction_lines:
    (count, frm, to) = map(int, line.replace('move', '').replace('from', '').replace ('to', '').split('  '))    
    
    for _ in range(count):
        stacks[to-1].insert(0, stacks[frm-1].pop(0))
      
print(''.join([stack[0] for stack in stacks]))