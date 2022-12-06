from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("TestUsername", 10, 700, 50)
        self.enemy_hero = Hero("TestEnemyUsername", 10, 600, 50)

    def test_correct_initialization(self):
        self.assertEqual("TestUsername", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(700, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_same_username_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_incorrect_hero_with_zero_hp_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_incorrect_enemy_hero_with_zero_hp_raise_value_error(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight TestEnemyUsername. He needs to rest", str(ve.exception))

    def test_heroes_hp_reduce_correctly_after_battle(self):
        self.hero.battle(self.enemy_hero)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(105, self.enemy_hero.health)

    def test_you_lose_battle_and_return_message(self):
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(55, self.enemy_hero.damage)
        self.assertEqual(result, "You lose")

    def test_you_win_battle_and_return_message(self):
        self.enemy_hero.health = 500

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(result, "You win")

    def test_draw_battle_and_return_message(self):
        self.hero.health = 500
        self.enemy_hero.health = 500

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_hero__str__(self):
        result = self.hero.__str__()

        self.assertEqual("Hero TestUsername: 10 lvl\nHealth: 700\nDamage: 50\n", result)


if __name__ == "__main__":
    main()
