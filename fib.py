# solution to http://rosalind.info/problems/fib/

from sys import argv


def rabbits(n, k):
    """
    >>> rabbits(5, 3)
    19
    """
    prev, nxt = 1, 1
    for _ in range(2, n):
        prev, nxt = nxt, prev * k + nxt
    return nxt


def main():
    script, input_file = argv

    with open(input_file, "r") as f:
        n, k = [int(i) for i in f.read().strip().split()]

    fname, s, ext = input_file.rpartition(".")
    output_file = fname + "_result" + s + ext

    with open(output_file, "w") as f:
        f.write(f"{rabbits(n, k)}")


if __name__ == "__main__":
    main()
