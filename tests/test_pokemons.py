import pytest
from exercises.pokemons import get_attack_value


def test_pokemons_with_correct_data():
    assert get_attack_value('fire', ['grass']) == 2
    assert get_attack_value('fighting', ['ice', 'rock']) == 4
    assert get_attack_value('psychic', ['poison', 'dark']) == 0
    assert get_attack_value('water', ['normal']) == 1
    assert get_attack_value('fire', ['rock']) == 0.5
