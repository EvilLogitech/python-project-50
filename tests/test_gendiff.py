import pytest
from gendiff import generate_diff
import os


tests_path = os.path.dirname(__file__)
testdata = [
    (f'{tests_path}/fixtures/examples/file1.json',
     f'{tests_path}/fixtures/examples/file2.json',
     'pass_stylish', 'stylish'),
    (f'{tests_path}/fixtures/examples/file1.yml',
     f'{tests_path}/fixtures/examples/file2.yaml',
     'pass_stylish', 'stylish'),
    (f'{tests_path}/fixtures/examples/file1.yml',
     f'{tests_path}/fixtures/examples/file2.json',
     'pass_stylish', 'stylish'),
    (f'{tests_path}/fixtures/examples/file1.json',
     f'{tests_path}/fixtures/examples/file2.json',
     'pass_plain', 'plain'),
    (f'{tests_path}/fixtures/examples/file1.json',
     f'{tests_path}/fixtures/examples/file2.json',
     'pass_json', 'json'),
    (f'{tests_path}/fixtures/examples/file1.json',
     f'{tests_path}/fixtures/examples/file2.json',
     'pass_stylish', 'stylish'),
    pytest.param(f'{tests_path}/fixtures/examples/file1.yml',
                 f'{tests_path}/fixtures/examples/file2.json',
                 'fail_stylish', 'stylish', marks=pytest.mark.xfail),
    pytest.param(f'{tests_path}/fixtures/examples/file1.json',
                 f'{tests_path}/fixtures/examples/file2.yaml',
                 'fail_json', 'json', marks=pytest.mark.xfail)
]


@pytest.mark.parametrize("file1,file2,expected_result,style",
                         testdata, indirect=["expected_result"]
                         )
def test_output(file1, file2, expected_result, style):
    diff = generate_diff(file1, file2, style)
    assert diff == expected_result
