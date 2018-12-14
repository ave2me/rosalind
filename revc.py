# solution to http://rosalind.info/problems/revc/

from sys import argv

COMPLEMENTS = "".maketrans("AGTC", "TCAG")


def revc(s):
    """
    >>> revc('AAAACCCGGT')
    'ACCGGGTTTT'
    """
    return s[::-1].translate(COMPLEMENTS)


def main():
    script, input_file = argv

    with open(input_file, "r") as f:
        seq = f.read()
        result = revc(seq)

    fname, s, ext = input_file.rpartition(".")
    output_file = fname + "_result" + s + ext

    with open(output_file, "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
