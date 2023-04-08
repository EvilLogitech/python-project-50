def get_string(pref, path, value1=None, value2=None):
    if isinstance(value1, dict):
        value1 = '[complex value]'
    if isinstance(value2, dict):
        value2 = '[complex value]'
    match pref:
        case 'added':
            return (f"Property '{'.'.join(path)}' was added "
                    f"with value: '{value1}'")
        case 'removed':
            return f"Property '{'.'.join(path)}' was removed"
        case 'updated':
            return (f"Property '{'.'.join(path)}' was updated. "
                    f"From '{value2}' to '{value1}'")


def get_formatted_string(diff):
    res = []

    def inner(inner_diff, inner_path):
        result = []
        current_path = inner_path
        for item in inner_diff:
            current_path.append(item['key'])
            match item['key_status']:
                case 'nested':
                    result.append(inner(item['children'], current_path))
                    current_path.pop()
                case 'unchanged':
                    current_path.pop()
                    pass
                case 'updated':
                    result.append(
                        get_string(item['key_status'],
                                   current_path, item['new_value'],
                                   item['old_value'])
                    )
                    current_path.pop()
                case _:
                    result.append(
                        get_string(item['key_status'],
                                   current_path,
                                   item['value'])
                    )
                    current_path.pop()
        return '\n'.join(result)
    res.append(inner(diff, []))
    return '\n'.join(res)
