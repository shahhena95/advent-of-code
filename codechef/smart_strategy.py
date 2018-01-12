#! python3


def strategy(x, d):
    product = 1
    for i in d:
        product *= i
    for i in range(0, len(x)):
        x[i] /= product
        print x[i],


def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, raw_input().split())
        d = map(int, raw_input().split())
        x = map(int, raw_input().split())
        strategy(x, d)

if __name__ == "__main__":
    main()
