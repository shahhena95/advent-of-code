with open('./inputs/day_02.txt') as f:
    instructions = f.readlines()

instructions = [map(int, line.strip('\n').split('x')) for line in instructions]


def get_paper_length():
    total_paper = 0
    for box in instructions:
        s1, s2, s3 = box[0] * box[1], box[1] * box[2], box[2] * box[0]
        smallest = min(s1, s2, s3)
        total_paper += 2 * (s1 + s2 + s3) + smallest

    print total_paper


def get_ribbon_length():
    total_ribbon = 0
    for box in instructions:
        box.sort()
        bow = box[0] * box[1] * box[2]
        smallest_perimeter = 2 * (box[0] + box[1])
        total_ribbon += bow + smallest_perimeter

    print total_ribbon

get_paper_length()
get_ribbon_length()
