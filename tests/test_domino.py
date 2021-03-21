import pytest
from exercises.domino import move_domino, move_domino_back
from exceptions import domino_exceptions


#  move_domino()

def test_with_correct_data():
    assert move_domino(r'||//||\||/\|', 1) == r'||///\\||/\|'
    assert move_domino(r'|\||\||/||\|', 2) == r'\\\\\||//\\|'
    assert move_domino(r'|\|\||||\/||', 4) == r'\\\\\\\\\///'


def test_with_zero_moves():
    assert move_domino(r'||//||\||/\|', 0) == r'||//||\||/\|'


def test_with_no_necessary_moves():
    assert move_domino(r'//////////', 10) == r'//////////'


def test_invalid_input_data_types_error_no_string():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino(1, 2)


def test_invalid_input_data_types_error_no_int():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino('///', 2.5)


def test_invalid_input_data_types_error_neg_int():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino('///', -2)


def test_empty_input_string_error():
    with pytest.raises(domino_exceptions.EmptyInputStringError):
        move_domino('', 5)


def test_not_allowable_char_error():
    with pytest.raises(domino_exceptions.NotAllowableCharError):
        move_domino(r'///a||\\\/|', 4)


# move_domino_back()

def test_back_with_correct_data():
    assert move_domino_back(r'||//|||', 1) == r'||/||||'
    assert move_domino_back(r'|||\\||', 1) == '||||\\||'


def test_back_corner_cases():
    assert move_domino_back(r'|//', 1) == '|/|'
    assert move_domino_back(r'\\|', 1) == '|\\|'


def test_back_with_zero_moves():
    assert move_domino_back(r'||//||\||/\|', 0) == r'||//||\||/\|'


def test_back_invalid_input_data_types_error_no_string():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino_back(1, 2)


def test_back_invalid_input_data_types_error_no_int():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino_back('///', 2.5)


def test_back_invalid_input_data_types_error_neg_int():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino_back('///', -2)


def test_back_empty_input_string_error():
    with pytest.raises(domino_exceptions.EmptyInputStringError):
        move_domino_back('', 5)


def test_back_not_allowable_char_error():
    with pytest.raises(domino_exceptions.NotAllowableCharError):
        move_domino_back(r'///a||\\\/|', 4)


def test_back_reverse_algorithm_not_possible_error1():
    with pytest.raises(domino_exceptions.ReverseAlgorithmNotPossibleError):
        move_domino_back(r'||///|//||', 1)


def test_back_reverse_algorithm_not_possible_error2():
    with pytest.raises(domino_exceptions.ReverseAlgorithmNotPossibleError):
        move_domino_back(r'|||//\\\||', 1)
