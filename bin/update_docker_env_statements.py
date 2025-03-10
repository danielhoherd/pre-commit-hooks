#!/usr/bin/env python3

import argparse
import re


def fix_dockerfile_line(line):
    pattern = r"^([Ee][Nn][Vv])\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+(.+)$"
    replacement = r"\1 \2=\3"
    return re.sub(pattern, replacement, line)


def main():
    parser = argparse.ArgumentParser(description="Make Dockerfile ENV vars conform to ENV key=val syntax.")
    parser.add_argument("filenames", nargs="+", help="Dockerfile(s) to process")
    args = parser.parse_args()

    for filename in args.filenames:
        with open(filename) as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                file.write(fix_dockerfile_line(line))


if __name__ == "__main__":
    main()
