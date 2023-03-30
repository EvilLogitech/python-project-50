import pytest
import os


tests_path = os.path.dirname(__file__)


@pytest.fixture
def expected_result(request):
    filepath = f'{tests_path}/fixtures/{request.param}'
    with open(filepath) as f:
        file_content = f.read()
    return file_content
