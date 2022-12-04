from project.cat import Cat


class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender=Tomcat.GENDER)

    def make_sound(self):
        return "Hiss"
