#!/usr/bin/env python3
# Sorts Ansible requirements.yml files
# https://galaxy.ansible.com/docs/using/installing.html

import sys
import yaml
import argparse


def sort_yaml(data):
    sorted_data = sorted(data, key=lambda record: record["name"])
    for entry in sorted_data:
        entry = sorted(entry)

    return yaml.safe_dump(sorted_data)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    retval = 0

    for filename in args.filenames:
        with open(filename, "r+") as f:
            input_yaml = yaml.safe_load(f)
            output_yaml = sort_yaml(input_yaml)
            if yaml.safe_dump(input_yaml) != output_yaml:
                print(f"Sorting contents of {filename}")
                f.seek(0)
                f.write("---\n" + output_yaml)
                f.truncate()

                retval = 1

    return retval


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
