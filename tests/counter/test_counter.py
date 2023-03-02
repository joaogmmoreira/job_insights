from src.pre_built.counter import count_ocurrences


def test_counter():
    count = count_ocurrences("tests/mocks/jobs.csv", "developer")
    assert count == 1
