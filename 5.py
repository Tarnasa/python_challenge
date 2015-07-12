__author__ = 'Tarnasa'

import pickle

with open('5.in', 'r') as f:
    x = pickle.loads('\n'.join(line.rstrip() for line in f.readlines()).encode('utf-8'))

a = ''

for line in x:
    for char, num in line:
        a += char * num
    a += '\n'

print(a)