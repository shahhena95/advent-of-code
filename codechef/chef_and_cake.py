#! python3
def modify_cake(cake, r, c):
    for i in range(r):
        cake[i] = list(cake[i])
        for j in range(c):
            if cake[i][j] == 'R':
                cake[i][j] = 0
            else:
                cake[i][j] = 1
    return cake


def cost(cake, r, c, parity):
    penalty = 0
    for i in range(r):
        for j in range(c):
            if ((i + j) & 1) == (cake[i][j] ^ parity):
                continue
            if cake[i][j] == 0:
                penalty += 5
            else:
                penalty += 3
    return penalty


def main():
    t = int(input())
    for _ in range(t):
        r, c = map(int, raw_input().split())
        cake = []
        for i in range(r):
            cake.append(raw_input())
        cake = modify_cake(cake, r, c)
        print (min(cost(cake, r, c, 0), cost(cake, r, c, 1)))


if __name__ == "__main__":
    main()
