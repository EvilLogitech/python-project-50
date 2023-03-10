#!/usr/bin/env python3


def parse(dict1, dict2):
    equal_keys = set(dict1.keys()) & set(dict2.keys())
    f1_keys = {('  - ', x) for x in (set(dict1.keys()) - equal_keys)}
    f2_keys = {('  + ', x) for x in (set(dict2.keys()) - equal_keys)}
    equal_keys = {('    ', x) for x in equal_keys}
    all_keys_list = sorted(f1_keys | f2_keys | equal_keys, key=lambda x: x[1])
    res = ['{']
    for prefix, key in all_keys_list:
        match prefix:
            case '  - ':
                res.append(f'{prefix}{key}: {dict1[key]}')
            case '  + ':
                res.append(f'{prefix}{key}: {dict2[key]}')
            case '    ':
                if dict1[key] == dict2[key]:
                    res.append(f'{prefix}{key}: {dict1[key]}')
                else:
                    res.append(f'  - {key}: {dict1[key]}')
                    res.append(f'  + {key}: {dict2[key]}')
    res.append('}')
    return '\n'.join(res).replace('True', 'true').replace('False', 'false')
