import pytest
from gendiff import generate_diff
from gendiff.utils.read_data import get_data_from_file
from gendiff.utils.formatting import formatting


testdata = [
    ('file1.json', 'file2.json', 'pass_stylish', 'stylish'),
    ('file1.yml', 'file2.yaml', 'pass_stylish', 'stylish'),
    ('file1.yml', 'file2.json', 'pass_stylish', 'stylish'),
    ('file1.json', 'file2.json', 'pass_plain', 'plain'),
    ('file1.json', 'file2.json', 'pass_json', 'json'),
    pytest.param('file1.yml', 'file2.json', 'fail_stylish',
                 'stylish', marks=pytest.mark.xfail),
    pytest.param('file1.json', 'file2.yaml', 'fail_json',
                 'json', marks=pytest.mark.xfail)
]


@pytest.mark.parametrize("file1, file2, expected_result, style", testdata,
                         indirect=['file1', 'file2', 'expected_result']
                         )
def test_output(file1, file2, expected_result, style):
    diff = generate_diff(file1, file2, style)
    assert diff == expected_result


def test_extension_exception():
    with pytest.raises(Exception):
        get_data_from_file('fail.txt')


def test_formatter_exception():
    with pytest.raises(Exception):
        formatting([], 'xml')
