import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

@pytest.fixture
def cliente_normal():
    from parking import Parking
    return Parking()

@pytest.fixture
def cliente_vip():
    from parking import Parking
    return Parking(vip=True)