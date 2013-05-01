import os
import sys
import re

def gen_dot(path='.'):
    print("digraph "+ path.replace("/", "_").replace(".", "_") + " {")
    FILE_FORMAT = r'[a-zA-Z0-9\-]+\.(h|c|(cpp)|(hpp))'
    FORMAT = r'#include (<|\")(.*)(>|\")'
    r = re.compile(FORMAT)
    for directory, subdirs, files in os.walk(path):
        for fname in files:
            if(re.match(FILE_FORMAT, fname)):
                with open(directory + "/" + fname, 'r') as f:
                    for line in f.readlines():
                        match = r.search(line)
                        if(match):
                            dep = match.group(2)
                            dep = re.search(FILE_FORMAT, dep).group().replace(".", "_")
                            print("\t" + fname.replace(".", "_") + " -> " + dep + ";")
    print("}")

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        for fil in sys.argv[1:]:
            gen_dot(fil)
    else:
        gen_dot()
