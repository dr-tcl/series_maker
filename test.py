import pytest
from main import series_maker


@pytest.mark.parametrize("number, answer",
                         [
                             (2, 1),
                             (6, 8),
                             (10, 10),
                             (1, 1),
                             (11, 8),
                             (12, 9)

                         ])
def test_cases(number, answer):
    assert series_maker(number) == answer
