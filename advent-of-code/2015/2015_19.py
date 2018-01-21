import re

#Referred to hints and solutions


def find_all_replacements(base_molecule, match, replace):
    indices = [m.start() for m in re.finditer(match, base_molecule)]
    lm = len(match)
    return [base_molecule[:i]+replace+base_molecule[i+lm:] for i in indices]

lines = [line for line in open('inputs/day_19.txt')]
base_molecule = lines[-1].strip()

molecules = set()
for line in lines:
    if '=>' not in line:
        continue
    match, _, replace = line.split()
    molecules.update(find_all_replacements(base_molecule, match, replace))
print(len(molecules))
