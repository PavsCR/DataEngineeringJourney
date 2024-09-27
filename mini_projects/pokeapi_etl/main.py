import requests

# Extract
def get_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    return response.json()

def get_ability_description(ability_url, language='en'):
    response = requests.get(ability_url)
    ability_data = response.json()

    for entry in ability_data['effect_entries']:
        if entry['language']['name'] == language:
            return entry['short_effect']
    return 'ability description not found'

# Transform
def get_abilities(pokemon_data):
    abilities = []
    for ability in pokemon_data['abilities']:
        ability_name = ability['ability']['name']
        ability_description = get_ability_description(ability['ability']['url'])

        abilities.append({
            'name': ability_name,
            'description': ability_description
        })
    return abilities

def get_stats(pokemon_data):
    stats = []
    for stat in pokemon_data['stats']:
        stats.append({
            'name': stat['stat']['name'],
            'value': stat['base_stat']
        })
    return stats

def transform_data(pokemon_data):
    return {
        'name': pokemon_data['name'],
        'types': [type['type']['name'] for type in pokemon_data['types']],
        'abilities': get_abilities(pokemon_data),
        'stats': get_stats(pokemon_data)
    }

# Load

pokemon_data = get_pokemon_data('pikachu')
transformed_data = transform_data(pokemon_data)
print(transformed_data)
