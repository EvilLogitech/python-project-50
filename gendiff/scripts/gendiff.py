#!/usr/bin/env python3
import argparse
import json
import yaml
from gendiff.scripts.comparator import get_raw_diff
from gendiff.scripts.formatter import stylish


def generate_diff(file_path1, file_path2):

    def get_data_from_file(file_path):
        extension = file_path[file_path.rindex('.'):]
        match extension:
            case '.yml' | '.yaml':
                with open(file_path) as f:
                    file_dict = yaml.safe_load(f)
            case '.json':
                with open(file_path) as f:
                    file_dict = json.load(f)
            case _:
                return
        return file_dict

    return get_raw_diff(
        get_data_from_file(file_path1),
        get_data_from_file(file_path2)
    )


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser._optionals.title = 'optional arguments'
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format",
                        help="set format of output",
                        default='stylish')
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)

    # diff = generate_diff('file1.json', 'file2.json')
    if args.format == 'stylish':
        result = stylish(diff)
    print(result)


if __name__ == "__main__":
    main()
