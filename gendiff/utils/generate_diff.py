from gendiff.utils.str_bool_lower import lower_bool_and_none
from gendiff.utils.comparator import build_nodes
from gendiff.utils.read_data import get_data_from_file
from gendiff.utils.formatting import formatting


@lower_bool_and_none
def generate_diff(file_path1, file_path2, format_name="stylish"):
    """
    This function returns string with the data difference between two files
    Target files may be: json, yaml
    Possible output formats: stylish, plain, json
    """
    diff = build_nodes(
        get_data_from_file(file_path1),
        get_data_from_file(file_path2)
    )
    return formatting(diff, format_name)
