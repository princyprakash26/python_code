# python program to replicate mv command:

import os
import sys

if len(sys.argv) != 2:
    print('check the command parameter')

fname = sys.argv[1]
cname = sys.argv[2]
try:
    inf = open(fname, 'r')
    text = inf.read()
    inf.close()

    os.replace(fname, cname)
    


except FileNotFoundError:
    print("File not Found")

