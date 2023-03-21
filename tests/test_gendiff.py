from gendiff.scripts.gendiff import generate_diff


with open('tests/fixtures/short_check_pass') as f:
    short_stylish_pass = f.read()
with open('tests/fixtures/short_check_fail') as f:
    short_fail_wrong_file_order = f.read()
with open('tests/fixtures/short_check_fail') as f:
    short_check_fail_equal_key = f.read()
with open('tests/fixtures/long_stylish_pass') as f:
    stylish_pass = f.read()
with open('tests/fixtures/long_stylish_fail') as f:
    stylish_fail = f.read()
with open('tests/fixtures/long_plain_pass') as f:
    plain_pass = f.read()
with open('tests/fixtures/long_plain_fail') as f:
    plain_fail = f.read()
with open('tests/fixtures/long_json_pass') as f:
    json_pass = f.read()


# PASS tests
def test_big_json_stylish_pass():
    diff = generate_diff('tests/fixtures/examples/file1.json',
                         'tests/fixtures/examples/file2.json',
                         'stylish')
    assert diff == stylish_pass


def test_big_yaml_stylish_pass():
    diff = generate_diff('tests/fixtures/examples/file1.yml',
                         'tests/fixtures/examples/file2.yaml',
                         'stylish')
    assert diff == stylish_pass


def test_big_json_yaml_stylish_pass():
    diff = generate_diff('tests/fixtures/examples/file1.json',
                         'tests/fixtures/examples/file2.json',
                         'stylish')
    assert diff == stylish_pass


def test_big_json_yaml_plain_pass():
    diff = generate_diff('tests/fixtures/examples/file1.json',
                         'tests/fixtures/examples/file2.json',
                         'plain')
    assert diff == plain_pass


def test_json_short_pass():
    diff = generate_diff('tests/fixtures/examples/file1_short.json',
                         'tests/fixtures/examples/file2_short.json',
                         'stylish')
    assert diff == short_stylish_pass


def test_yaml_short_pass():
    diff = generate_diff('tests/fixtures/examples/file1_short.yaml',
                         'tests/fixtures/examples/file2_short.yml',
                         'stylish')
    assert diff == short_stylish_pass


def test_json_yaml_short_pass():
    diff = generate_diff('tests/fixtures/examples/file1_short.json',
                         'tests/fixtures/examples/file2_short.yml',
                         'stylish')
    assert diff == short_stylish_pass


def test_json_output_pass():
    diff = generate_diff('tests/fixtures/examples/file1.json',
                         'tests/fixtures/examples/file2.json',
                         'json')
    assert diff == json_pass


# Fail tests
def test_json_short_fail():
    diff = generate_diff('tests/fixtures/examples/file1_short.json',
                         'tests/fixtures/examples/file2_short.json',
                         'stylish')
    assert diff != short_fail_wrong_file_order


def test_yaml_short_fail():
    diff = generate_diff('tests/fixtures/examples/file1_short.yaml',
                         'tests/fixtures/examples/file2_short.yml',
                         'stylish')
    assert diff != short_fail_wrong_file_order


def test_short_file_order_fail():
    diff = generate_diff('tests/fixtures/examples/file1_short.json',
                         'tests/fixtures/examples/file2_short.json',
                         'stylish')
    assert diff != short_check_fail_equal_key


def test_big_json_yaml_stylish_fail():
    diff = generate_diff('tests/fixtures/examples/file1.json',
                         'tests/fixtures/examples/file2.json',
                         'stylish')
    assert diff != stylish_fail


def test_big_json_yaml_plain_fail():
    diff = generate_diff('tests/fixtures/examples/file1.json',
                         'tests/fixtures/examples/file2.json',
                         'plain')
    assert diff != plain_fail
