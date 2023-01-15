from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("TestTeamOne")
        # self.team.members = {"MemberOneTeamOne": 25}

        self.team2 = Team("TestTeamTwo")
        # self.members = {"MemberOneTeamTwo": 20}

    def test_correct_initialization(self):
        self.assertEqual("TestTeamOne", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_initialization_name_contains_non_alpha_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team = Team("Team1")

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_members_if_does_not_exist_and_returns_message(self):
        self.team.members = {"MemberOne": 25}
        members_to_add = {"MemberOne": 25, "MemberTwo": 20}
        result = self.team.add_member(**members_to_add)

        self.assertEqual("Successfully added: MemberTwo", result)
        self.assertEqual({"MemberOne": 25, "MemberTwo": 20}, self.team.members)

    def test_remove_existing_member_and_returns_message(self):
        self.team.members = {"MemberOne": 25, "MemberTwo": 20}

        result = self.team.remove_member("MemberOne")

        self.assertEqual("Member MemberOne removed", result)
        self.assertEqual({"MemberTwo": 20}, self.team.members)

    def test_remove_non_existing_member_and_returns_message(self):
        self.team.members = {"MemberOne": 25}

        result = self.team.remove_member("MemberTwo")

        self.assertEqual("Member with name MemberTwo does not exist", result)
        self.assertEqual({"MemberOne": 25}, self.team.members)

    def test_greater_than_when_greater(self):
        self.team.members = {"MemberOne": 25, "MemberTwo": 20}
        self.team2.members = {"MemberOne": 22}

        self.assertEqual(True, self.team > self.team2)

    def test_greater_than_when_not_greater(self):
        self.team.members = {"MemberOne": 25}
        self.team2.members = {"MemberOne": 22, "MemberTwo": 20}

        self.assertEqual(False, self.team > self.team2)

    def test__len__method(self):
        self.team.members = {"MemberOne": 25, "MemberTwo": 20}

        result = len(self.team)

        self.assertEqual(2, result)

    def test__add__method(self):
        self.team.members = {"MemberOne": 25, "MemberThree": 30}
        self.team2.members = {"MemberOne": 22, "MemberTwo": 20}

        new_team = self.team + self.team2

        self.assertEqual("TestTeamOneTestTeamTwo", new_team.name)
        self.assertEqual({'MemberThree': 30, 'MemberOne': 25, 'MemberTwo': 20}, new_team.members)

    def test__str__method(self):
        self.team.members = {"B": 30, "A": 30, "C": 20}

        result = str(self.team)

        self.assertEqual("Team name: TestTeamOne\n"
                         "Member: A - 30-years old\n"
                         "Member: B - 30-years old\n"
                         "Member: C - 20-years old", result)


if __name__ == '__main__':
    main()
