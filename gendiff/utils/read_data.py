import json
import yaml


def get_data_from_file(file_path):
    extension = file_path[file_path.rindex('.'):]
    match extension:
        case '.yml' | '.yaml':
            with open(file_path) as f:
                file_dict = yaml.safe_load(f)
        case '.json':
            with open(file_path) as f:
                file_dict = json.load(f)
        case _:
            raise Exception('Invalid file type. Support json and yaml')
    return file_dict
