import sys
from geo import add


def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return 

    a, b = map(int, data[:2])
    result = add(a, b)
    print(result)


if __name__ == "__main__":
    main()
