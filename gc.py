# solution to http://rosalind.info/problems/gc/

from sys import argv

script, input_file, *rest = argv

def is_fasta(s):
    return s.startswith('>Rosalind_')

def clean(s):
    return s[1:]

with open(input_file, 'r') as ipf:
    lines = (line.strip() for line in ipf.read())

data = {}
for item in lines:
    if is_fasta(item):
        data[clean(item)] = next(lines)

print(data)