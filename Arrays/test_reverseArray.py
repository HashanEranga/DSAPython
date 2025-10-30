import pytest
from reverseArray import reverseArray

def test_reverseArray():
    assert reverseArray([10,11,12]) == [12,11,10]
    assert reverseArray([]) == []
    assert reverseArray([12]) == [12]
