from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        try:
            pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
        except StopIteration:
            return f"Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = []

        result.append(f"Pokemon Trainer {self.name}")
        result.append(f"Pokemon count {len(self.pokemons)}")
        [result.append(f"- {x.pokemon_details()}") for x in self.pokemons]

        return '\n'.join(result)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
