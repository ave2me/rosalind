# solution to http://rosalind.info/problems/dna/

from collections import Counter
from sys import argv

ANSWER_TEMPLATE = "{A:d} {C:d} {G:d} {T:d}"


def count(seq):
    """
    >>> count('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    '20 12 17 21'
    """
    cnt = Counter(seq)
    return ANSWER_TEMPLATE.format(**cnt)


def main():
    script, input_file = argv

    with open(input_file) as f:
        seq = f.read()
        result = count(seq)

    fname, s, ext = input_file.rpartition(".")
    output_file = fname + "_result" + s + ext

    with open(output_file, "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
