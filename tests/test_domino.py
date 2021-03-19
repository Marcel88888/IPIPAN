import pytest
from exercises.domino import move_domino
from exceptions import domino_exceptions


def test_domino_with_correct_data():
    arrangement1 = move_domino(r'||//||\||/\|', 1)
    assert arrangement1 == r'||///\\||/\|'

    arrangement2 = move_domino(r'|\||\||/||\|', 2)
    assert arrangement2 == r'\\\\\||//\\|'

    arrangement3 = move_domino(r'|\|\||||\/||', 4)
    assert arrangement3 == r'\\\\\\\\\///'


def test_domino_with_zero_moves():
    arrangement1 = move_domino(r'||//||\||/\|', 0)
    assert arrangement1 == r'||//||\||/\|'


def test_domino_with_no_necessary_moves():
    arrangement = move_domino(r'//////////', 10)
    assert arrangement == r'//////////'


def test_domino_invalid_input_data_types_error_no_string():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino(1, 2)


def test_domino_invalid_input_data_types_error2_no_int():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino('///', 2.5)


def test_domino_invalid_input_data_types_error_neg_int():
    with pytest.raises(domino_exceptions.InvalidInputDataTypesError):
        move_domino('///', -2)


def test_domino_empty_input_string_error():
    with pytest.raises(domino_exceptions.EmptyInputStringError):
        move_domino('', 5)


def test_domino_not_allowable_char_error():
    with pytest.raises(domino_exceptions.NotAllowableCharError):
        move_domino(r'///a||\\\/|', 4)


