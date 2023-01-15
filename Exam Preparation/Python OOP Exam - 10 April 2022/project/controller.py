class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def find_supply_by_type(self, supply_type):
        for supply in self.supplies:
            if supply.__class__.__name__ == supply_type:
                return supply

    def __take_last_supply_by_type(self, supply_type):
        for idx in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[idx]).__name__ == supply_type:
                return self.supplies.pop(idx)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def add_player(self, *players):  # player1: Player, player2: Player...
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):  # supply1: Supply, supply2: Supply...
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        current_player = self.__find_player_by_name(player_name)
        if current_player.stamina == 100:
            return f"{player_name} have enough stamina."

        current_supply = self.__take_last_supply_by_type(sustenance_type)
        if current_supply:
            current_player._sustain_player(current_supply)

            return f"{player_name} sustained successfully with {current_supply.name}."

    @staticmethod
    def __check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1 < p2:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        current_first_player = self.__find_player_by_name(first_player_name)
        current_second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_if_the_players_cannot_duel(current_first_player, current_second_player)
        if result:
            return result

        if current_first_player < current_second_player:
            return self.__attack(current_first_player, current_second_player)
        else:
            return self.__attack(current_second_player, current_first_player)

    def next_day(self):
        for player in self.players:
            player.stamina = max(0, player.stamina - player.age * 2)

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []

        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)
