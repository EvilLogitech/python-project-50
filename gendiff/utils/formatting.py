import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain
import gendiff.formatters.json as json


def formatting(diff, format_name):
    match format_name:
        case 'stylish':
            formatter = stylish
        case 'plain':
            formatter = plain
        case 'json':
            formatter = json
        case _:
            raise Exception(
                'Unknown formatter name. Please choose: json, plain, stylish'
            )
    return formatter.get_formatted_string(diff)
