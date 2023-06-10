
import sys

if len(sys.argv) != 2:
    print('Check the parameter command')

fname = sys.argv[1]
nname = sys.argv[2]
try:
    inf = open(fname, 'r')
    text = inf.read()
    inf.close()
    new = open(nname, 'w')
    new.write(text)

except FileNotFoundError:
        print("File not found")
