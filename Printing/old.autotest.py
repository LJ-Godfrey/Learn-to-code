# This code is to simply test whether your output is correct or not
# No need to read this file

import sys
import os

from helloworld import helloWorld
from inputOutput import inputoutput

GREEN = '\033[92m'
RED = '\033[91m'
NORMAL = '\033[0m'

PY_PATHS = ["/usr/bin/python3", "/usr/local/bin/python3"]
# 1. Check if user has python3
def pyCheck(paths):
	found = -1
	for path in paths:
		if os.path.exists(path): 
			return path

	if not found >= 0:
		return -1
'''
def helloCheck():
    if helloWorld() == "Hello World!\n":
        print(helloWorld())
        return True
    else:
        return False
'''
def helloCheck():
    path = pyCheck(PY_PATHS)
    if path > -1:
        os.system(path + ' helloworld.py > /tmp/hellotest.txt')
    f = open('/tmp/hellotest.txt', 'r')
    line = f.readline()
    print(line)
    if line == "Hello World!":
        return True
    else:
        return False


def ioCheck():
    tests = ['Test', 'Ethan', 'User!!?34', 'sfdhk\n', '\tHi?']
    for test in tests:
        if inputoutput(test) != 'Hello ' + test + '!':
            return False
    return True

def passed(test):
    print(test + '\t[' + GREEN + 'passed' + NORMAL + ']')

def failed(test):
    print(test + '\t[' + RED + 'failed' + NORMAL + ']')


print("Running autotests...")
pcount = 0
fcount = 0
if helloCheck:
    passed('helloWorld')
    pcount += 1
else:
    failed('helloWorld')
    fcount += 1

if ioCheck:
    passed('inputOutput')
    pcount += 1
else:
    failed('inputOutput')
    fcount += 1
if fcount > 0:
    failed('\n{}/{} tests'.format(fcount, fcount + pcount))
else:
    passed('\n{}/{} tests'.format(pcount, pcount + fcount))