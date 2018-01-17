import itertools


def process_input():
    with open('./inputs/day_13.txt') as f:
        instructions = f.readlines()

    instructions = [line.strip('.\n').split() for line in instructions]

    knights, people = {}, set()
    for line in instructions:
        knights[(line[0], line[-1])] = get_happiness(line)
        people.add(line[0])

    return people, knights


def get_happiness(line):
    return int('-'+line[3]) if line[2] == 'lose' else int(line[3])


def calculate_happiness(chart, arrangement):
    happiness = 0
    l = len(arrangement)
    for i in range(0, l):
        happiness += chart[(arrangement[i % l], arrangement[(i + 1) % l])]
        happiness += chart[(arrangement[(i + 1) % l], arrangement[i % l])]

    return happiness


def maximize_happiness(people, chart):
    permutations = list(itertools.permutations(list(people)))
    all_happiness = []
    for arrangement in permutations:
        all_happiness.append(calculate_happiness(chart, arrangement))

    print max(all_happiness)


def seat_myself(people, chart):
    for person in people:
        chart[('Me', person)] = 0
        chart[(person, 'Me')] = 0

    people.add('Me')
    maximize_happiness(people, chart)


if __name__ == "__main__":
    people, chart = process_input()
    maximize_happiness(people, chart)
    seat_myself(people, chart)
