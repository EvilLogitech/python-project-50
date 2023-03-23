import re


def lower_bool_and_none(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        result = result.replace("False", 'false')
        result = result.replace("True", 'true')
        result = result.replace("None", 'null')
        result = result.replace("'false'", 'false')
        result = result.replace("'true'", 'true')
        result = result.replace("'null'", 'null')
        result = result.replace('"false"', 'false')
        result = result.replace('"true"', 'true')
        result = result.replace('"null"', 'null')
        result = result.replace("'[complex value]'", '[complex value]')
        result = re.sub(r'(\'|")(\d+\.?\d?)("|\')', r'\2', result)
        return result
    return inner
