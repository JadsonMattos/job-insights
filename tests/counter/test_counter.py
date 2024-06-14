from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    words = ['Python', 'JavaScript']
    for word in words:
        assert count_ocurrences(path, word) >= 0
        assert count_ocurrences(
            path, word.lower()) == count_ocurrences(path, word.upper())
