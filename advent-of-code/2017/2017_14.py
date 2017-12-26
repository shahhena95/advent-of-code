def reverse_sublist(std_list, start, end):
    if start <= end:
        std_list[start:end] = std_list[start:end][::-1]
        return std_list
    else:
        reverse = std_list[start:] + std_list[:end]
        reverse = reverse[::-1]
        std_list[start:], std_list[:end] = reverse[:256-start], reverse[256-start:]
        return std_list


def sparse_hash(sequence):
    std_list = list(range(256))
    skip_size = 0
    current_pos = 0
    for i in range(0, 64):
        for length in sequence:
            start = current_pos % 256
            if start + length < 256:
                std_list = reverse_sublist(std_list, start, start + length)
            else:
                std_list = reverse_sublist(std_list, start, (start + length) - 256)

            current_pos += length + skip_size
            skip_size += 1

    return std_list


def xor_list(input_list):
    result = 0
    for x in input_list:
        result ^= x
    return result


def dense_hash(sparse_hash):
    dense_hash_list = []
    i = 0
    #looks very unpleasant. can be optimized?
    while i < 256:
        dense_hash_list.append(xor_list(sparse_hash[i:i+16]))
        i += 16

    dense_hash_list = [
                       hex(dense_hash_list[i])[2:].zfill(2)
                       for i in range(len(dense_hash_list))
                       ]

    return ''.join(dense_hash_list)


def disk():
    hashes = []
    for row in range(0, 128):
        sparse = sparse_hash(map(ord, "hfdlxzhv-"+str(row)) + [17, 31, 73, 47, 23])
        dense = dense_hash(sparse)
        bin_hash = bin(int(dense, 16))[2:].zfill(128)
        for column, x in enumerate(bin_hash):
            if x == '1':
                hashes.append((row, column))
    return hashes


hashes = disk()
print(len(hashes))


adjacent = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(root):
    queue = [root]
    while queue:
        (x, y) = queue.pop()
        for neighbour_x, neighbour_y in adjacent:
            neighbour = x + neighbour_x, y + neighbour_y
            if neighbour in hashes:
                queue.append(neighbour)
                hashes.remove(neighbour)


#improve dfs for connected components
def count_regions(hashes):
    regions = 0
    while hashes:
        dfs(hashes.pop())
        regions += 1
    return regions

print(count_regions(hashes))
