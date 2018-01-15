with open('./inputs/day_05.txt') as f:
    instructions = f.readlines()

instructions = [line.strip('\n') for line in instructions]

vowels = ['a', 'e', 'i', 'o', 'u']
disallowed = ['ab', 'cd', 'pq', 'xy']


def vowel_check(string):
    count = 0
    for letter in vowels:
        if letter in string:
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


def solve(part=1):
    count = 0
    for string in instructions:
        if vowel_check(string) and double_letter_check(string) and check_disallowed(string):
            count += 1

    return count

# print solve()
print vowel_check("aaa")
print double_letter_check("aaa")
print check_disallowed("aaa")
