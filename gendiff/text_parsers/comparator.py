def get_raw_diff(dict1, dict2):
    diff = []
    all_keys_list = sorted(set(dict1.keys()) | set(dict2.keys()))
    for key in all_keys_list:
        k1, k2 = dict1.get(key), dict2.get(key)
        if not (key in dict1):
            diff.append(('added', key, k2))
        elif not (key in dict2):
            diff.append(('removed', key, k1))
        elif k1 == k2:
            diff.append(('same', key, k1))
        else:
            if isinstance(k1, dict) and isinstance(k2, dict):
                diff.append(('indent', key, get_raw_diff(k1, k2)))
            else:
                diff.append(('upd_f1', key, k1))
                diff.append(('upd_f2', key, k2))
    return diff
