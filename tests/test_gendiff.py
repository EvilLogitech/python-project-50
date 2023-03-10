from gendiff.scripts.gendiff import generate_diff


with open('tests/fixtures/plain_check_pass') as f:
    string_plain_pass = f.read()
with open('tests/fixtures/plain_check_fail') as f:
    string_test_fail_wrong_file_order = f.read()
with open('tests/fixtures/plain_check_fail') as f:
    plain_check_fail_equal_key = f.read()


def test_json_pass():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == string_plain_pass


def test_yaml_pass():
    diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
    assert diff == string_plain_pass


def test_json_yaml_pass():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yml')
    assert diff == string_plain_pass


def test_json_fail():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff != string_test_fail_wrong_file_order


def test_yaml_fail():
    diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
    assert diff != string_test_fail_wrong_file_order


def test_file_order_fail():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff != plain_check_fail_equal_key
