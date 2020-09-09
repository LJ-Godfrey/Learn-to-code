import os

GREEN = '\033[92m'
RED = '\033[91m'
NORMAL = '\033[0m'

def pyCheck(paths):
	found = -1
	for path in paths:
		if os.path.exists(path): 
			return path

	if not found >= 0:
		return -1

PY_PATHS = ["/usr/bin/python3", "/usr/local/bin/python3"]
PATH = pyCheck(PY_PATHS)

def passed(test):
    print(test + '\t[' + GREEN + 'passed' + NORMAL + ']')

def failed(test):
    print(test + '\t[' + RED + 'failed' + NORMAL + ']')

# This only works for a program that just prints stuff
def print_prog(name):
    os.system(PATH + " " + name + ".py > /tmp/" + name + ".test")

def inp_prog(name, infile):
    os.system(PATH + " " + name + ".py < " + infile + " > /tmp/" + name + ".test")

def out_check(name, expected):
    f = open("/tmp/" + name + ".test", 'r')
    out = ''.join(f.readlines())
    out = out[:len(out)-1]
    if out == expected:
        passed(name)
    else:
        failed(name)
        print("\nYour output: \n\t{} \nExpected output: \n\t{}".format(out, expected))
