# solution to http://rosalind.info/problems/rna/

from sys import argv

DNA_TO_RNA = "".maketrans("T", "U")


def to_rna(s):
    """
    >>> to_rna('GATGGAACTTGACTACGTAAATT')
    'GAUGGAACUUGACUACGUAAAUU'
    """
    return s.translate(DNA_TO_RNA)


def main():
    script, input_file = argv

    with open(input_file) as f:
        dna = f.read()

    result = to_rna(dna)

    fname, s, ext = input_file.rpartition(".")
    output_file = fname + "_result" + s + ext

    with open(output_file, "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
