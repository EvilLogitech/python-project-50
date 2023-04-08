import itertools


prefix = {
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    ',
    'nested': '    '
}


def parse_value(some_dict, depth):

    def walk_dict(node, depth):
        if not isinstance(node, dict):
            return str(node)
        res = []
        value_indent = depth * prefix['nested']
        bracket_ident = (depth - 1) * prefix['nested']
        for key, value in node.items():
            res.append(f'{value_indent}{key}: '
                       f'{walk_dict(value, depth + 1)}')
        result = itertools.chain('{', res, [bracket_ident + '}'])
        return '\n'.join(result)
    return walk_dict(some_dict, depth + 2)


def get_formatted_string(diff):

    def walk(inner_diff, depth):
        depth_pref = depth * prefix['nested']
        result = ['{']
        for item in inner_diff:
            match item['key_status']:
                case 'nested':
                    result.append(
                        f'{depth_pref}{prefix[item["key_status"]]}'
                        f'{item["key"]}: '
                        f'{walk(item["children"], depth + 1)}'
                    )
                case 'updated':
                    result.append(
                        f'{depth_pref}{prefix["removed"]}'
                        f'{item["key"]}: '
                        f'{parse_value(item["old_value"], depth)}'
                    )
                    result.append(
                        f'{depth_pref}{prefix["added"]}'
                        f'{item["key"]}: '
                        f'{parse_value(item["new_value"], depth)}'
                    )
                case _:
                    result.append(
                        f'{depth_pref}{prefix[item["key_status"]]}'
                        f'{item["key"]}: '
                        f'{parse_value(item["value"], depth)}')
        result.append(f'{depth_pref}}}')
        return '\n'.join(result)
    return walk(diff, 0)
