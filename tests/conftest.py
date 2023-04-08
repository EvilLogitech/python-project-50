import pytest
import os


tests_path = os.path.dirname(__file__)


@pytest.fixture
def file1(request):
    filepath = f'{tests_path}/fixtures/examples/{request.param}'
    return filepath


@pytest.fixture
def file2(request):
    filepath = f'{tests_path}/fixtures/examples/{request.param}'
    return filepath


@pytest.fixture
def expected_result(request):
    filepath = f'{tests_path}/fixtures/{request.param}'
    with open(filepath) as f:
        file_data = f.read()
    return file_data
