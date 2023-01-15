from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []    # contains all the horses as objects
        self.jockeys = []   # # contains all the jockeys as objects
        self.horse_races = []   # contains all the horse races as objects

    def __find_if_horse_exists_and_return_it(self, horse_name: str):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse
        return

    def __find_if_jockey_exists_and_return_it(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return

    def __check_if_horse_race_already_exists_by_type(self, horse_race_type: str):
        for horse_race in self.horse_races:
            if horse_race.race_type == horse_race_type:
                return horse_race
        return

    def __find_horse_by_type_and_return_last_added_horse_of_type(self, horse_type: str):
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    return horse
        return

    def __find_horse_by_type_and_return_last_added_horse(self, horse_type: str):
        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    return horse
        return

    @staticmethod
    def __find_winner_and_return_it(jockeys):
        speed = 0
        winner = None

        for jockey in jockeys:
            if jockey.horse.speed > speed:
                speed = jockey.horse.speed
                winner = jockey

        return winner, speed

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return

        if self.__find_if_horse_exists_and_return_it(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__find_if_jockey_exists_and_return_it(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__check_if_horse_race_already_exists_by_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_if_jockey_exists_and_return_it(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.__find_horse_by_type_and_return_last_added_horse(horse_type)

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__check_if_horse_race_already_exists_by_type(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__find_if_jockey_exists_and_return_it(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        else:
            horse_race.jockeys.append(jockey)

            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__check_if_horse_race_already_exists_by_type(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner, speed = self.__find_winner_and_return_it(horse_race.jockeys)

        return f"The winner of the {race_type} race, with a speed of {speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."
