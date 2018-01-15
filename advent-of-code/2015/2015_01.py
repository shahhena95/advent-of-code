from collections import deque

with open('./inputs/day_01.txt') as f:
    instructions = f.readlines()


def count_floors(stack=deque()):
    [stack.appendleft(1) if char == '(' else stack.appendleft(-1) for char in instructions[0]]
    return sum(stack)


def find_basement(instructions, stack=deque()):
    for i in range(len(instructions)):
        if instructions[i] == '(':
            stack.appendleft(1)
        elif len(stack) == 0:
            return i+1
        else:
            stack.popleft()

print count_floors()
print find_basement(instructions[0])
