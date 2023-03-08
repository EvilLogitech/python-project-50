import argparse
import json


def generate_diff(file_path1, file_path2):
    prefix = {
        'file1': '  - ',
        'file2': '  + ',
        'both': '    '
    }
    file1_json = json.load(open(file_path1))
    file2_json = json.load(open(file_path2))
    all_keys = sorted(set(file1_json.keys()) | set(file2_json.keys()))
    res = ['{']
    for key in all_keys:
        if (key in file1_json) and (key in file2_json):
            if file1_json[key] == file2_json[key]:
                res.append(f"{prefix['both']}{key}: {file1_json[key]}")
            else:
                res.append(f"{prefix['file1']}{key}: {file1_json[key]}")
                res.append(f"{prefix['file2']}{key}: {file2_json[key]}")
        elif key in file1_json:
            res.append(f"{prefix['file1']}{key}: {file1_json[key]}")
        else:
            res.append(f"{prefix['file2']}{key}: {file2_json[key]}")
    res.append('}')
    return '\n'.join(res)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser._optionals.title = 'optional arguments'
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
