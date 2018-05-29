# solution to http://rosalind.info/problems/revc/

from sys import argv

script, input_file, * = argv

COMPLEMENTS = ''.maketrans('AGTC', 'TCAG')

def revc(s):
    return s[::-1].translate(COMPLEMENTS)

with open(input_file, 'r') as ifp:
    seq = ifp.read()
    result = revc(seq)

fname, s, ext = input_file.rpartition('.')
output_file = fname + '_result' + s + ext

with open(output_file, 'w') as ofp:
    ofp.write(result)
