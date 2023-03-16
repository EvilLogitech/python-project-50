def get_string(pref, path, value1=None, value2=None):
    match pref:
        case 'added':
            return (f"Property '{'.'.join(path)}' was added "
                    f"with value: '{value1}'")
        case 'removed':
            return f"Property '{'.'.join(path)}' was removed"
        case 'upd_f2':
            return (f"Property '{'.'.join(path)}' was updated. "
                    f"From '{value2}' to '{value1}'")


def get_formatted_string(diff):

    def inner(inner_diff, inner_path):
        result = []
        pre_value = []

        def walk(node, path):
            res = []
            res_path = []
            if path:
                res_path.extend(path)
            pref, key, value = node
            res_path.append(key)
            if isinstance(value, dict):
                value = '[complex value]'
            match pref:
                case 'same':
                    return
                case 'added':
                    return get_string(pref, res_path, value)
                case 'removed':
                    return get_string(pref, res_path)
                case 'upd_f1':
                    pre_value.append(value)
                    return
                case 'upd_f2':
                    return get_string(pref, res_path, value, pre_value.pop())
                case 'indent':
                    y = inner(value, res_path)
                    if y:
                        res.append(y)
            return '\n'.join(res)
        for item in inner_diff:
            result.append(walk(item, inner_path))
        final_list = list(filter((lambda x: x), result))
        return '\n'.join(final_list)
    return inner(diff, [])
