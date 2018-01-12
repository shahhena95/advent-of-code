def turing():
    steps = 12399302
    state_dict = {'A': ((1, 1, 'B'), (0, 1, 'C')),
                  'B': ((0, -1, 'A'), (0, 1, 'D')),
                  'C': ((1, 1, 'D'), (1, 1, 'A')),
                  'D': ((1, -1, 'E'), (0, -1, 'D')),
                  'E': ((1, 1, 'F'), (1, -1, 'B')),
                  'F': ((1, 1, 'A'), (1, 1, 'E'))
                  }
    state = 'A'
    position = 0
    tape = [0] * steps
    for _ in range(steps):
        value = tape[position]
        write, move, state = state_dict[state][value]
        tape[position] = write
        position += move

    print(sum(tape))
if __name__ == '__main__':
    turing()
