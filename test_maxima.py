from maxima import find_maxima


def test_simple_sequence_two_maxima():
    inp = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima(inp)
    exp = [2, 4]
    assert exp == out


def test_simple_sequence_one_maxima():
    inp = [-i ** 2 for i in range(-3, 4)]
    out = find_maxima(inp)
    exp = [3]
    assert exp == out


def test_max_on_both_borders():
    inp = [4, 2, 1, 3, 1, 2]
    out = find_maxima(inp)
    exp = [0, 3, 5]
