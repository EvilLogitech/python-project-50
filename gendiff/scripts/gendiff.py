import argparse
import json


def generate_diff(file_path1, file_path2):
    file1_json = json.load(open(file_path1))
    file2_json = json.load(open(file_path2))
    equal_keys = set(file1_json.keys()) & set(file2_json.keys())
    f1_keys = {('  - ', x) for x in (set(file1_json.keys()) - equal_keys)}
    f2_keys = {('  + ', x) for x in (set(file2_json.keys()) - equal_keys)}
    equal_keys = {('    ', x) for x in equal_keys}
    all_keys_list = sorted(f1_keys | f2_keys | equal_keys, key=lambda x: x[1])
    res = ['{']
    for prefix, key in all_keys_list:
        match prefix:
            case '  - ':
                res.append(f'{prefix}{key}: {file1_json[key]}')
            case '  + ':
                res.append(f'{prefix}{key}: {file2_json[key]}')
            case '    ':
                if file1_json[key] == file2_json[key]:
                    res.append(f'{prefix}{key}: {file1_json[key]}')
                else:
                    res.append(f'  - {key}: {file1_json[key]}')
                    res.append(f'  + {key}: {file2_json[key]}')
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
    # diff = generate_diff('file1.json', 'file2.json')
    print(diff)


if __name__ == "__main__":
    main()
