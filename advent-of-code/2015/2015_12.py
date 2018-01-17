import re
import json


with open('./inputs/day_12.txt') as f:
    instructions = f.read()

print "part1", sum(map(int, re.findall(r'[+-]?\d+(?:\.\d+)?', instructions)))


def part_2(instructions):
    if "red" in instructions.values(): return {}
    else: return instructions

clean_red = str(json.loads(instructions, object_hook=part_2))
print "part2", sum(map(int, re.findall(r'[+-]?\d+(?:\.\d+)?', clean_red)))
