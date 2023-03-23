import itertools


prefix = {
    'added': '  + ',
    'removed': '  - ',
    'upd_f1': '  - ',
    'upd_f2': '  + ',
    'same': '    ',
    'indent': '    '
}


def parse_dict(some_dict, depth):

    def walk_dict(node, depth):
        if not isinstance(node, dict):
            return str(node)
        res = []
        value_indent = depth * prefix['indent']
        bracket_ident = (depth - 1) * prefix['indent']
        for key, value in node.items():
            res.append(f'{value_indent}{key}: '
                       f'{walk_dict(value, depth + 1)}')
        result = itertools.chain('{', res, [bracket_ident + '}'])
        return '\n'.join(result)

    res_str = walk_dict(some_dict, depth)
    # return, removing first bracket in dict string
    return res_str[res_str.find('\n') + 1:]


def get_formatted_string(diff):

    def walk(node, depth):
        res = ['{']
        depth_pref = depth * prefix['indent']
        for item in node:
            pref, key, value = item
            res_prefix = depth_pref + prefix[pref]
            if not isinstance(value, list):
                if isinstance(value, dict):
                    res.append(f'{res_prefix}{key}: {{\n'
                               f'{parse_dict(value, depth + 2)}')
                else:
                    res.append(f'{res_prefix}{key}: {value}')
            else:
                res.append(f'{res_prefix}{key}: {walk(value, depth + 1)}')
        res.append(f'{depth_pref}}}')
        return '\n'.join(res)
    return walk(diff, 0)
