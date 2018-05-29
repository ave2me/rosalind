# solution to http://rosalind.info/problems/dna/

from collections import Counter
from sys import argv

template = '{A:d} {C:d} {G:d} {T:d}'

script, input_file, * = argv

def count(seq):
    '''s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    >>>count(s)
    '20 12 17 21'
    '''
    cnt = Counter(seq)
    return template.format(**cnt)

with open(input_file) as ifp:
    seq = ifp.read()
    result = count(seq)

fname, s, ext = input_file.rpartition('.')
output_file = fname + '_result' + s + ext

with open(output_file, 'w') as ofp:
    ofp.write(result)
