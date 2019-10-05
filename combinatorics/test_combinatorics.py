import pytest
from combinatorics import permutations, combinations, variations_without_repetition, variations_with_repetition

def test_permutations_of_non_numeric_throws_exception():
    with pytest.raises(Exception):
        permutations([])

def test_permutations_of_n_options():
    assert permutations(10) == 3628800

def test_combinations_of_non_numeric_sample_throws_exception():
    with pytest.raises(Exception):
        combinations({}, 5)

def test_combinations_of_non_numeric_selection_throws_exception():
    with pytest.raises(Exception):
        combinations(5, {})
    
def test_combinations():
    assert combinations(15, 2) == 105

def test_variation_without_repetition_of_non_numeric_sample_throws_exception():
    with pytest.raises(Exception):
        variations_without_repetition({}, 5)

def test_variation_without_repetition_of_non_numeric_selection_throws_exception():
    with pytest.raises(Exception):
        variations_without_repetition(5, {})

def test_variations_without_repetition():
    assert variations_without_repetition(15, 2) == 210

def test_variation_with_repetition_of_non_numeric_sample_throws_exception():
    with pytest.raises(Exception):
        variations_with_repetition({}, 5)

def test_variation_with_repetition_of_non_numeric_selection_throws_exception():
    with pytest.raises(Exception):
        variations_with_repetition(5, {})

def test_variations_with_repetition():
    assert variations_with_repetition(15, 2) == 225