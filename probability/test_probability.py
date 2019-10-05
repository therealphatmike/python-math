import pytest
from probability import basic_probability

def test_empty_sample_space():
    with pytest.raises(Exception):
        # 0 represents empty sample space
        basic_probability(2, 0)
    
def test_no_preferred_outcomes():
    assert basic_probability(0, 50) == 0

def test_basic_probability_value():
    assert basic_probability(25, 100) == 0.25