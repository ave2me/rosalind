# solution to http://rosalind.info/problems/rna/

from sys import argv

DNA_TO_RNA = ''.maketrans('T', 'U')

script, input_file, * = argv

with open(input_file) as ipf:
    t = ipf.read()
    result = t.translate(DNA_TO_RNA)

fname, s, ext = input_file.rpartition('.')
output_file = fname + '_result' + s + ext

with open(output_file, 'w') as ofp:
    ofp.write(result)
