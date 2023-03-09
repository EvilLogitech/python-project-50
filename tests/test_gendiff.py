from gendiff.gendiff import generate_diff


def test_plain_diff():
    diff = generate_diff('file1.json', 'file2.json')
    with open('tests/fixtures/plain_check_string') as f:
        test_string = f.read()
        assert diff == test_string
