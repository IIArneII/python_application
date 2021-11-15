from os import listdir
from os.path import isfile, join
import hashlib

path = 'D:\\рэ'
files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

ht = {}
for path in files:
    f = open(path, 'rb')
    lines = b''.join(f.readlines())
    f.close()
    h = hashlib.sha1()
    h.update(lines)
    if h.hexdigest() not in ht:
        ht[h.hexdigest()] = []
    ht[h.hexdigest()].append(path)
for i in ht:
    if len(ht[i]) > 1:
        print('\n', i, ':', sep='')
        for j in ht[i]:
            print('\t', j)
