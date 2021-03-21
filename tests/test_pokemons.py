import pytest
from exercises.pokemons import get_attack_value
from exceptions import pokemons_exceptions


def test_with_correct_data():
    assert get_attack_value('fire', ['grass']) == 2
    assert get_attack_value('fighting', ['ice', 'rock']) == 4
    assert get_attack_value('psychic', ['poison', 'dark']) == 0
    assert get_attack_value('water', ['normal']) == 1
    assert get_attack_value('fire', ['rock']) == 0.5
    assert get_attack_value('fire', ['bug', 'steel', 'grass', 'rock']) == 4


def test_invalid_input_data_types_error_without_str():
    with pytest.raises(pokemons_exceptions.InvalidInputDataTypesError):
        get_attack_value(4, ['ice', 'rock'])


def test_invalid_input_data_types_error_without_list():
    with pytest.raises(pokemons_exceptions.InvalidInputDataTypesError):
        get_attack_value('fire', 'ice')


def test_invalid_input_data_types_error_without_str_in_list():
    with pytest.raises(pokemons_exceptions.InvalidInputDataTypesError):
        get_attack_value('fire', ['rock', 2])


def test_empty_str():
    with pytest.raises(pokemons_exceptions.EmptyInputStringError):
        get_attack_value('', ['rock'])


def test_empty_str_in_list():
    with pytest.raises(pokemons_exceptions.EmptyInputStringError):
        get_attack_value('rock', ['rock', '', 'ice'])


def test_with_unknown_type():
    with pytest.raises(pokemons_exceptions.AttackNotDefinedError):
        get_attack_value('rock', ['ice', 'fjklbwes'])
