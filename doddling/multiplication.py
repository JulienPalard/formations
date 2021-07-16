from hypothesis import given
from hypothesis.strategies import integers


def russian_multiplication(x, y):
    columns = [(x, y)]
    while x >= 1:
        columns.append((x := x // 2, y := y * 2))
    return sum(y for x, y in columns if x % 2)


def egyptian_multiplication(x, y):
    i = 1
    values = [y]
    while i < x:
        i *= 2
        values.append((y := y * 2))
    return sum(x for b, x in zip(reversed(f"{x:b}"), values) if b == '1')


@given(integers(min_value=0), integers(min_value=0))
def test_russian_multiplication(x, y):
    assert russian_multiplication(x, y) == x * y


@given(integers(min_value=0), integers(min_value=0))
def test_egyptian_multiplication(x, y):
    assert egyptian_multiplication(x, y) == x * y
