import re, sys

str = ''
eval = ''
rev_count = 0

with open('./inputs/day_08.txt') as f:
    for line in f:
        line = line.rstrip()

        str += line
        eval += line[1:-1]
        rev_count += line.count('\\') + line.count('"') + len(line) + 2

eval = re.sub(r'\\x..|\\.', '*', eval)

print(len(str) - len(eval))
print rev_count - len(str)
