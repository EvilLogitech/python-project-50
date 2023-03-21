#!/usr/bin/env python3
import argparse
import json
import yaml
from gendiff.text_parsers.comparator import get_raw_diff
import gendiff.text_parsers.formatter_stylish as f_stylish
import gendiff.text_parsers.formatter_plain as f_plain
import gendiff.text_parsers.formatter_json as f_json
from gendiff.text_parsers.str_bool_lower import lower_bool_and_none


@lower_bool_and_none
def generate_diff(file_path1, file_path2, format_name):

    def get_data_from_file(file_path):
        extension = file_path[file_path.rindex('.'):]
        match extension:
            case '.yml' | '.yaml':
                with open(file_path) as f:
                    file_dict = yaml.safe_load(f)
            case '.json':
                with open(file_path) as f:
                    file_dict = json.load(f)
        return file_dict
    diff = get_raw_diff(
        get_data_from_file(file_path1),
        get_data_from_file(file_path2)
    )
    match format_name:
        case 'stylish':
            formatter = f_stylish
        case 'plain':
            formatter = f_plain
        case 'json':
            formatter = f_json
    return formatter.get_formatted_string(diff)


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
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
