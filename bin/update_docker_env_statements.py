#!/usr/bin/env python3

import argparse
import os
import re
import sys


def fix_dockerfile_line(line):
    pattern = r"^([Ee][Nn][Vv])\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+(.+)$"
    replacement = r"\1 \2=\3"
    return re.sub(pattern, replacement, line)


def main():
    parser = argparse.ArgumentParser(description="Make Dockerfile ENV vars conform to ENV key=val syntax.")
    parser.add_argument("filenames", nargs="+", help="Dockerfile(s) to process")
    args = parser.parse_args()

    if not args.filenames:
        raise SystemExit(0)

    for filename in args.filenames:
        if not os.path.exists(filename):
            print(f"ERROR: file not found: {filename}", file=sys.stderr)
            continue
        with open(filename) as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                file.write(fix_dockerfile_line(line))


if __name__ == "__main__":
    main()
