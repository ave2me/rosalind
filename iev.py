# solution to http://rosalind.info/problems/iev/

from operator import mul
from sys import argv

WEIGHTS = [2, 2, 2, 1.5, 1, 0]


def expected_offspring(pairs):
    """
    >>> expected_offspring([1, 0, 0, 1, 0, 1])
    3.5
    >>> expected_offspring([17104, 17940, 18905, 17472, 17027, 18553])
    151133.0
    """
    return sum(mul(p, w) for p, w in zip(pairs, WEIGHTS))


def main():
    script, *_pairs = argv
    pairs = [int(p) for p in _pairs]
    print(expected_offspring(pairs))


if __name__ == "__main__":
    main()
