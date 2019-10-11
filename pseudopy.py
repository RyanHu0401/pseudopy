#!/usr/local/bin/python3
"""YEAH"""

import sys
import string
import argparse

def pystrtolist(code:str):
    """Parse a code given in string and returns key words"""
    flist = [] # the final returned list of keywords
    current_group = [] # the currently parsed words
    line_continuation = False # if '\' is used for line continuation
    is_string = False # if is currently parsing string
    for counter in range(len(code)):
        char = code[char]
        if is_string == True: # test for if parsing string
            if char == "\\": # remember this is for '\' for escaping backslash
                current_group.append(char)
            elif char in ["'", '"']: # test for quotes
                if
            current_group.append(char)
        elif char in string.ascii_letters + ["_"]: # if is common namespace
            current_group.append(char)
        elif char in ["\n", " ", ";"]: # if is EOL, EOS, EOW
            if current_group: # append current namespace to flist
                flist.append("".join(current_group))
                current_group = []
            if char == "\n":
                if not line_continuation:
                    flist.append(";")
                else:
                    line_continuation = False
            elif char == ";":
                flist.append(";")
        elif char == "\\":
            line_continuation = True
    if flist[-1] != ";":
        flist.append(";")

def py2pseudo(code:str, indent=4):
    """Main function"""
    fstring = string.strip() # remove useless parts of the code
    codelist = pystrtolist(code) # parse the code into separate strings

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            "pseudopy"
            description="A parser/compiler of Python <==> Pseudocode for saving IG/AS/AL students (i hope)"
            )
    parser.add_argument("-t", "--text", nargs="?")
    parser.add_argument("-i", "--indent", nargs="?", default=4, type=int)
    arguments = parser.parse_args(sys.argv[1:])

    py2pseudo(fcode, indent = arguments.indent)
