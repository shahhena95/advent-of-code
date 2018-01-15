with open('./inputs/day_05.txt') as f:
    instructions = f.readlines()

instructions = [line.strip('\n') for line in instructions]

vowels = ['a', 'e', 'i', 'o', 'u']
disallowed = ['ab', 'cd', 'pq', 'xy']


def vowel_check(string):
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1

    if count >= 3:
       return True
    return False


def double_letter_check(string):
    for i in range(0, len(string)-1):
        char = string[i]+string[i]
        if char in string:
            return True
    return False


def check_disallowed(string):
    for char in disallowed:
        if char in string:
            return False

    return True


def part1():
    count = 0
    for string in instructions:
        if vowel_check(string) and double_letter_check(string) and check_disallowed(string):
            count += 1

    return count

print part1()


def check_double_pairs(string):
    for i in range(0, len(string)-1):
        char = string[i:i+2]
        if char in string[i:]:
            if char in string[i+2:]:
                return True
    return False


def check_in_between(string):
    for i in range(0, len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


def part2():
    count = 0
    for string in instructions:
        if check_double_pairs(string) and check_in_between(string):
            count += 1

    return count

print part2()