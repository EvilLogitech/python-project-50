def build_nodes(dict1, dict2):
    """
    This function returns difference between two files
    """
    nodes = []
    all_keys_list = sorted(set(dict1.keys()) | set(dict2.keys()))
    for key in all_keys_list:
        k1, k2 = dict1.get(key), dict2.get(key)
        if not (key in dict1):
            nodes.append({'key_status': 'added', 'key': key, 'value': k2})
        elif not (key in dict2):
            nodes.append({'key_status': 'removed', 'key': key, 'value': k1})
        elif k1 == k2:
            nodes.append({'key_status': 'unchanged', 'key': key, 'value': k1})
        else:
            if isinstance(k1, dict) and isinstance(k2, dict):
                nodes.append(
                    {'key_status': 'nested',
                     'key': key,
                     'children': build_nodes(k1, k2)}
                )
            else:
                nodes.append(
                    {'key_status': 'updated',
                     'key': key,
                     'old_value': k1,
                     'new_value': k2}
                )
    return nodes
