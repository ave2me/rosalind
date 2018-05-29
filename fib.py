# solution to http://rosalind.info/problems/fib/

from sys import argv

script, input_file, *rest = argv

with open(input_file, 'r') as ipf:
    n, k = [int(i) for i in ifp.read().strip().split()]

def rabbits(n, k):
    kids = 1
    adults = 1
    for _ in range(2, n):
        newborn = adults * k
        adults += kids
        kids = newborn
    return adults + kids

fname, s, ext = input_file.rpartition('.')
output_file = fname + '_result' + s + ext

with open(output_file, 'w') as opf:
    print(rabbits(gen, num))
    opf.write(f'{rabbits(gen, num)}')