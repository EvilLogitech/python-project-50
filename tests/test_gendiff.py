from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.formatter import stylish as format_diff


with open('tests/fixtures/plain_check_pass') as f:
    string_plain_pass = f.read()
with open('tests/fixtures/plain_check_fail') as f:
    string_test_fail_wrong_file_order = f.read()
with open('tests/fixtures/plain_check_fail') as f:
    plain_check_fail_equal_key = f.read()
with open('tests/fixtures/recursive_pass') as f:
    recursive_pass = f.read()
with open('tests/fixtures/recursive_fail') as f:
    recursive_fail = f.read()


def test_big_json_pass():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert format_diff(diff) == recursive_pass


def test_big_yaml_pass():
    diff = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml')
    assert format_diff(diff) == recursive_pass


def test_big_json_yaml_pass():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert format_diff(diff) == recursive_pass


def test_json_short_pass():
    diff = generate_diff('tests/fixtures/file1_short.json', 'tests/fixtures/file2_short.json')
    assert format_diff(diff) == string_plain_pass


def test_yaml_short_pass():
    diff = generate_diff('tests/fixtures/file1_short.yaml', 'tests/fixtures/file2_short.yml')
    assert format_diff(diff) == string_plain_pass


def test_json_yaml_short_pass():
    diff = generate_diff('tests/fixtures/file1_short.json', 'tests/fixtures/file2_short.yml')
    assert format_diff(diff) == string_plain_pass


def test_json_short_fail():
    diff = generate_diff('tests/fixtures/file1_short.json', 'tests/fixtures/file2_short.json')
    assert format_diff(diff) != string_test_fail_wrong_file_order


def test_yaml_short_fail():
    diff = generate_diff('tests/fixtures/file1_short.yaml', 'tests/fixtures/file2_short.yml')
    assert format_diff(diff) != string_test_fail_wrong_file_order


def test_file_order_fail():
    diff = generate_diff('tests/fixtures/file1_short.json', 'tests/fixtures/file2_short.json')
    assert format_diff(diff) != plain_check_fail_equal_key
