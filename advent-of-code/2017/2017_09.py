import sys
sys.path.insert(0, "/Library/Python/2.7/site-packages") #acod
sys.path.insert(0, "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python") #acod dependency
import aocd


def get_data():
    return aocd.get_data("53616c7465645f5f51687d84c2dfe78a29cc10b8f7229b420668017a5b0fabfaeb360c5a2cd461d5f5898982f5a5db94", 9, 2017)


def process_stream(stream):
    i = 0
    in_garbage = 0
    nesting_level = 0
    groups = 0
    while i < len(stream):
        if stream[i] == '<':
            i += 1
            while stream[i] != '>':

                if stream[i] == '!':
                    i += 1
                else:
                    in_garbage += 1
                i += 1

        if stream[i] == '{':
            nesting_level += 1
        if stream[i] == '}':
            groups += nesting_level
            nesting_level -= 1

        i += 1
    return groups, in_garbage


def main():
    stream = get_data()
    print(process_stream(stream))


if __name__ == "__main__":
    main()
