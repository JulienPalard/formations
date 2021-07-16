from hypothesis import given, settings, Verbosity
from hypothesis.strategies import booleans

# Monoid({True, False}, and)

s = {True, False}


@given(booleans(), booleans())
@settings(verbosity=Verbosity.debug)
def test_internal_composition_law(b1, b2):
    assert (b1 and b2) in s
    assert (b1 or b2) in s


@given(booleans(), booleans())
def test_commutative(b1, b2):
    assert (b1 and b2) == (b2 and b1)
    assert (b1 or b2) == (b2 or b1)


@given(booleans(), booleans(), booleans())
def test_associative(b1, b2, b3):
    assert (b1 and (b2 and b3)) == ((b1 and b2) and b3)
    assert (b1 or (b2 or b3)) == ((b1 or b2) or b3)


@given(booleans())
def test_neutral_element(b1):
    assert (b1 and True) == b1
    assert (b1 or False) == b1
