import requests
from exceptions import pokemons_exceptions


def check_input(att_type, def_types):
    """
    Checks if the given parameters are correct.
    :param str att_type: type of the attack
    :param int def_types: type(s) of the pokemon under attack
    :raise:
        pokemons_exceptions.InvalidInputDataTypesError if 'att_type' is not a str or 'def_types' is not a list or
    'def_types' contains elements which are not strings
        pokemons_exceptions.EmptyInputStringError if 'att_type' is an empty str or 'def_types' contains empty strings
    """
    if not isinstance(att_type, str) or not isinstance(def_types, list) or \
            any(not isinstance(def_type, str) for def_type in def_types):
        raise pokemons_exceptions.InvalidInputDataTypesError()
    if not att_type or '' in def_types:
        raise pokemons_exceptions.EmptyInputStringError()


def get_attack_value(att_type, def_types):
    """
    Based on the type of movement (attack), it calculates the effectiveness (damage factor) against a pokemon of a given
    type (or types).
    :param str att_type: type of the attack
    :param list def_types: type(s) of the pokemon under attack
    :raise pokemons_exceptions.AttackNotDefinedError if there is not a pokemon type given in the 'def_types'
    :return int/float: effectiveness (damage factor) of the attack
    """
    check_input(att_type, def_types)
    url_with_no_type = f"https://pokeapi.co/api/v2/type/"
    url = url_with_no_type + f"{att_type}"
    response = requests.get(url)
    data = response.json()
    damage_relations = data['damage_relations']
    damages = []
    damage_types = {
        key: [damage_type['name'] for damage_type in damage_relations[key]]
        for key in damage_relations.keys()
    }

    poss_pos_att_values = {  # possible positive attack values
        'double_damage_to': 2,
        'half_damage_to': 0.5
    }

    for def_type in def_types:
        found = False
        if def_type in damage_types['no_damage_to']:
            return 0
        for attack_key in poss_pos_att_values.keys():
            if def_type in damage_types[attack_key]:
                found = True
                damages.append(poss_pos_att_values[attack_key])
                break
        if not found and requests.get(url_with_no_type + f'{def_type}').status_code != 200:
            raise pokemons_exceptions.AttackNotDefinedError(def_type)

    attack_value = 1
    for damage in damages:
        attack_value *= damage

    return attack_value
