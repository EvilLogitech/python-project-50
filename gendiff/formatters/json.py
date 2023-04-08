keys_status = {
    'added': '"keyStatus":"added"',
    'removed': '"keyStatus":"removed"',
    'updated': '"keyStatus":"updated"',
    'unchanged': '"keyStatus":"unchanged"',
    'nested': '"keyStatus":"nested"'
}


def get_parsed_value(some_value):
    """
    returns json pairs of key-value with double quotes (or full dictionaries)
    """
    if not isinstance(some_value, dict):
        return f'"{str(some_value)}"'

    def walk_dict(node):
        if not isinstance(node, dict):
            return f'"{str(node)}"'
        res = []
        for key, value in node.items():
            res.append(f'"{key}":{walk_dict(value)},')
        return f'{{{"".join(res)}}}'
    res_str = walk_dict(some_value)
    return res_str


def get_json_result_string(some_string):
    """
    Transform bad raw string into valid human-readable json string.
    Adds indents, transforms string-numbers to normal numbers, removes commas
    """
    indent = '    '
    result = ''
    depth = 0
    pre_string = some_string.replace(',,', ',')
    pre_string = pre_string.replace(',]', ']')
    pre_string = pre_string.replace(',}', '}')
    for char in pre_string:
        match char:
            case ('[' | '{'):
                result += char
                depth += 1
                result += f'\n{depth * indent}'
            case (']' | '}'):
                depth -= 1
                result += f'\n{depth * indent}'
                result += char
            case ',':
                result += char
                result += f'\n{depth * indent}'
            case _:
                result += char
    return result


def get_raw_string(diff):
    """
    returns single-line bad json string with commas after each value
    """
    def parse_diff(node):
        res = []
        for item in node:
            match item['key_status']:
                case 'nested':
                    res.append(
                        f'{{{keys_status["nested"]},'
                        f'"key":"{item["key"]}",'
                        f'"children":['
                        f'{parse_diff(item["children"])}]}},'
                    )
                case 'updated':
                    res.append(
                        f'{{{keys_status["updated"]},'
                        f'"key":"{item["key"]}",'
                        f'"oldValue":{get_parsed_value(item["old_value"])},'
                        f'"newValue":{get_parsed_value(item["new_value"])}}},'
                    )
                case _:
                    res.append(
                        f'{{{keys_status[item["key_status"]]},'
                        f'"key":"{item["key"]}",'
                        f'"value":{get_parsed_value(item["value"])}}},'
                    )
        return ''.join(res)
    result = ['[', parse_diff(diff), ']']
    return ''.join(result)


def get_formatted_string(diff):
    """
    Main function of module. Returns valid multi-line json string
    """
    result = get_raw_string(diff)
    return get_json_result_string(result)
