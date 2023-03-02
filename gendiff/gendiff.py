import argparse


parser = argparse.ArgumentParser(
        prog = 'gendiff',
        description = 'Compares two configuration files and shows a difference.',
        )
parser._optionals.title = 'optional arguments'
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.parse_args()
