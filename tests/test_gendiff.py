from gendiff.scripts.gendiff import generate_diff


def test_plain_diff():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    with open('tests/fixtures/plain_check_string') as f:
        test_string = f.read()
    assert diff == test_string
