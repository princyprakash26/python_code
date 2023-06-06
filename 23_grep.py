# python program to replicate grep command

import sys

if len(sys.argv) != 3 :
    print('Check the command parameter')
phrase = sys.argv[1]
phrase = phrase.lower()
fname = sys.argv[2]

try:
    with open(fname, 'r') as f:
        text=f.read()

    if phrase in text.lower() :
        print(f'phrase {phrase} is {text.index(phrase)}')

except FileNotFoundError:
    print('The file name is not found')