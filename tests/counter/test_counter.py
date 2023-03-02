from src.pre_built.counter import count_ocurrences


def test_counter():
    count = count_ocurrences("data/jobs.csv", "python")
    assert count == 1639
