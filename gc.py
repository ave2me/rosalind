# solution to http://rosalind.info/problems/gc/

from sys import argv


def is_fasta(s):
    """
    >>> is_fasta('>Rosalind_4120')
    True

    >>> is_fasta('>NotFasta_7832')
    False
    """
    return s.startswith(">Rosalind_")


def get_label(s):
    """
    >>> get_label('>Rosalind_4120')
    'Rosalind_4120'
    """
    return s[1:]


def parse_strings(lines):
    """
    >>> parse_strings(['>Rosalind_4120', 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAA', 'CCGTTTCTCTGAGGCTTCCGGCCTT', 'CCCTCCCACTAATAATTCTGAGG'])
    {'Rosalind_4120': 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'}
    """
    data = {}
    for line in lines:
        if is_fasta(line):
            label = get_label(line)
            continue
        data[label] = data.get(label, "") + line.strip()
    return data


def gc_content(s):
    """
    >>> gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT')
    60.9195
    """
    cont = (s.count("G") + s.count("C")) / len(s) * 100
    return round(cont, 4)


def calc_gc_content(strings):
    """
    >>> calc_gc_content({'Rosalind_4120': 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'})
    {'Rosalind_4120': 53.75}
    """
    return {k: gc_content(v) for k, v in strings.items()}


def main():
    script, input_file = argv

    with open(input_file, "r") as f:
        lines = (line.rstrip() for line in f.readlines())

    strings = parse_strings(lines)
    gc_contents = calc_gc_content(strings)

    label, max_content = max(gc_contents.items(), key=lambda item: item[1])

    print("{0}\n{1}".format(label, max_content))


if __name__ == "__main__":
    main()
