import sys

if len(sys.argv) != 2:
    print('Check the parameter command')
for i in range(1,len(sys.argv)):
    fname = sys.argv[i]
try:

    inf = open(fname, 'r')
    for line in inf:
        print(line,end='')

    inf.close()
except FileNotFoundError:
    print('Files are is not found')
