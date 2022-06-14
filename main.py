import requests
import random

pokemon_id = random.choice(range(1, 152))
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
pokemon_data = response.json()

print(f"You got pokemon number {pokemon_data['id']}, {pokemon_data['name'].capitalize()}!")
print(f"Height: {pokemon_data['height']} | weight: {pokemon_data['weight']}")

pokemon_types = []

for type_data in pokemon_data['types']:
    pokemon_types.append(type_data['type']['name'])

print(f"Types: {', '.join(pokemon_types)}")

pokemon_abilities = []

for ability_data in pokemon_data['abilities']:
    pokemon_abilities.append(ability_data['ability']['name'])

print(f"Abilities: {', '.join(pokemon_abilities)}")
