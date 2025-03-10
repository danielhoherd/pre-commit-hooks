#!/usr/bin/env python3

import re
import sys


def fix_dockerfile_line(line):
    pattern = r"^([Ee][Nn][Vv])\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+(.+)$"
    replacement = r"\1 \2=\3"
    return re.sub(pattern, replacement, line)


def main():
    for filename in sys.argv[1:]:
        with open(filename) as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                file.write(fix_dockerfile_line(line))


if __name__ == "__main__":
    main()
