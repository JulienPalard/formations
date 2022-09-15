from bisect import bisect_left
import pytest
from hypothesis.strategies import lists, integers
from hypothesis import given

def reference_index(a_list, a_value):
    """Locate the leftmost value exactly equal to a_value.

    This one is from docs.python.org.
    """
    i = bisect_left(a_list, a_value)
    if i != len(a_list) and a_list[i] == a_value:
        return i
    raise ValueError


def index(a_list, a_value):
    """Locate the leftmost value exactly equal to a_value."""
    begin, end = 0, len(a_list)
    while (end - begin) > 1:  # Search in a_list[begin:end]
        middle = (end + begin) // 2
        if a_list[middle] > a_value:
            end = middle
        else:
            begin = middle
    if len(a_list) and a_list[begin] == a_value:
        return begin
    raise ValueError


def dumb_index(a_list, a_value):
    """Locate the leftmost value exactly equal to a_value."""
    for i in a_list:
        if i == a_value:
            return i
    raise ValueError


@pytest.mark.parametrize("function", [dumb_index, index, index])
def test_index(function):
    assert index([1, 2, 3], 1) == 0
    assert index([1, 2, 3], 2) == 1
    assert index([1, 2, 3], 3) == 2

    with pytest.raises(ValueError):
        assert index([1, 2, 3], 1.1)
    with pytest.raises(ValueError):
        assert index([1, 2, 3], 2.1)
    with pytest.raises(ValueError):
        assert index([1, 2, 3], 3.1)



@given(lists(integers()), integers())
def test_hypo(l, i):
    l.sort()
    try:
        reference_index(l, i)
    except ValueError:
        value_error = True
    else:
        value_error = False
    if value_error:
        with pytest.raises(ValueError):
            index(l, i)
    else:
        assert reference_index(l, i) == index(l, i) == dumb_index(l, i)
