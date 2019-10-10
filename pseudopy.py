#!/usr/local/bin/python3

import sys
import string
import argparse

def pystrtolist(code):
    flist = []
    current_group = []
    line_continuation = False
    for char in code:
        if char in string.ascii_letters + ["_"]:
            current_group.append(char)
        elif char in ["\n", " "]:
            if current_group:
                flist.append(current_group)
                current_group = []
        elif char == "\\":
            line_continuation = True
                
def py2pseudo(string:str):
    fstring = string.strip()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            "pseudopy"
            description="A parser/compiler of Python <==> Pseudocode for saving IG/AS/AL students (i hope)"
            )
    parser.add_argument("-i", "--indent", nargs="?", default=4, type=int)
    arguments = parser.parse_args(sys.argv[1:])
