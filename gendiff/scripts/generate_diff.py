import json
import yaml
import gendiff.formatters.f_stylish as f_stylish
import gendiff.formatters.f_plain as f_plain
import gendiff.formatters.f_json as f_json
from gendiff.utils.str_bool_lower import lower_bool_and_none
from gendiff.utils.comparator import get_raw_diff


@lower_bool_and_none
def generate_diff(file_path1, file_path2, format_name="stylish"):
    """
    This function returns string with the data difference between two files
    Target files may be: json, yaml
    Possible output formats: stylish, plain, json
    """

    def get_data_from_file(file_path):
        extension = file_path[file_path.rindex('.'):]
        match extension:
            case '.yml' | '.yaml':
                with open(file_path) as f:
                    file_dict = yaml.safe_load(f)
            case '.json':
                with open(file_path) as f:
                    file_dict = json.load(f)
        return file_dict
    diff = get_raw_diff(
        get_data_from_file(file_path1),
        get_data_from_file(file_path2)
    )
    match format_name:
        case 'stylish':
            formatter = f_stylish
        case 'plain':
            formatter = f_plain
        case 'json':
            formatter = f_json
    return formatter.get_formatted_string(diff)
