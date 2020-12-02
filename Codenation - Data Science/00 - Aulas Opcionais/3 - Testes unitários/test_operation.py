from startapi import operation
import pytest

def test_op_mean():
    assert operation.op_mean([1, 2, 3, 4]) == pytest.approx(2.5)