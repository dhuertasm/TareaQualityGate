import pytest
from src import app

def test_suma():
    assert app.suma(1,1) == 2
