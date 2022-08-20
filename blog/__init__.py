import sys

sys.setrecursionlimit(1000000)


def main():
    def _input_numbers():
        return list(map(int, sys.stdin.readline().split()))


if __name__ == '__main__':
    main()
