#!/usr/bin/env python3
# Sorts Ansible requirements.yml files
# https://galaxy.ansible.com/docs/using/installing.html

import sys
import yaml
import argparse


def sort_data(data):
    return_data = []
    sorted_data = sorted(data, key=lambda record: record["name"])

    for entry in sorted_data:
        sorted_keys = sorted(entry)
        return_data.append({key: entry[key] for key in sorted_keys})

    return sorted_data


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    retval = 0

    for filename in args.filenames:
        with open(filename, "r+") as f:
            original_file_content = f.read()
            input_data = yaml.safe_load(original_file_content)
            output_data_dumped = "---\n" + yaml.safe_dump(sort_data(input_data))
            if original_file_content != output_data_dumped:
                print(f"Sorting contents of {filename}")
                f.seek(0)
                f.write(output_data_dumped)
                f.truncate()

                retval = 1

    return retval


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
