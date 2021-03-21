import requests
from exceptions import pokemons_exceptions


def check_input(att_type, def_types):
    if not isinstance(att_type, str) or not isinstance(def_types, list) or \
            any(not isinstance(def_type, str) for def_type in def_types):
        raise pokemons_exceptions.InvalidInputDataTypesError()
    if not att_type or '' in def_types:
        raise pokemons_exceptions.EmptyInputStringError()


def get_attack_value(att_type, def_types):
    check_input(att_type, def_types)
    url = f"https://pokeapi.co/api/v2/type/{att_type}"
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
        if def_type in damage_types['no_damage_to']:
            return 0
        for attack_key in poss_pos_att_values.keys():
            if def_type in damage_types[attack_key]:
                damages.append(poss_pos_att_values[attack_key])

    attack_value = 1
    for damage in damages:
        attack_value *= damage

    return attack_value
