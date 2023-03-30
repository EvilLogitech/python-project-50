#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.scripts.cli import parse_cli_args


def main():
    args = parse_cli_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
